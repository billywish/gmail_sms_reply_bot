from gmail.mark_as_unread import mark_email_as_unread
from db import update_email_status
from gmail.send_email import send_email
from util.log import log
from util.draft_save_notify import redraft_save_notify
from models import EmailStatus
from ai.response_parser import parse_user_response_with_openai
from sms.format_instructions import send_reply_format_instructions

class ConfirmationResponseHandler:
    def __init__(self, email_id, response, feedback, email_record):
        self.email_id = email_id
        self.response = response
        self.feedback = feedback
        self.email_record = email_record

    def handle_response(self):
        """Main entry point for handling a user response."""
        normalized_response = self.response.lower()
        feedback = self.feedback

        if normalized_response not in ('y', 'n', 'r'):
            log(f"Unrecognized response '{self.response}' for email id {self.email_id}, trying OpenAI parsing...")
            intent, parsed_feedback = parse_user_response_with_openai(self.response)
            normalized_response = intent.lower()
            feedback = parsed_feedback or feedback
            log(f"OpenAI parsed intent: {intent}, feedback: {parsed_feedback}")

        if normalized_response == 'y':
            self.handle_approval()
        elif normalized_response == 'n':
            self.handle_discard()
        elif normalized_response == 'r':
            self.handle_redraft(feedback)
        else:
            self.handle_invalid()

    def handle_approval(self):
        """Send approved email and update the record status to SENT"""
        send_email(
            self.email_record['recipient'],
            f"Subject: {self.email_record['subject']}\n\n{self.email_record['generated_reply']}",
            self.email_record['message_id']
        )
        update_email_status(self.email_id, EmailStatus.SENT)
        log(f"Email sent for id {self.email_id}")

    def handle_discard(self):
        """Update the record status to DISCARDED and mark the email in the gmail inbox as unread"""
        update_email_status(self.email_id, EmailStatus.DISCARDED)
        log(f"Email discarded for id {self.email_id}")
        # will this be picked back up once its marked as unread?
        # mark_email_as_unread(self.email_id)

    def handle_redraft(self, feedback):
        """Redraft with provided feedback, save a new pending draft, and notify via sms"""
        if not feedback:
            log(f"Email rejected for id {self.email_id} but no feedback provided.")
            return
        update_email_status(self.email_id, EmailStatus.REJECTED)
        log(f"Email rejected for id {self.email_id}, refining draft with feedback.")

        new_email_id = redraft_save_notify(self.email_record, feedback)
        log(f"New draft saved and SMS sent with ID {new_email_id}")

    def handle_invalid(self):
        """Invalid response. Send reply format instructions."""
        log(f"Unable to parse response for email id {self.email_id}. Sending format instructions.")
        send_reply_format_instructions()
