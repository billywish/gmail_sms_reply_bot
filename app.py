import threading
import time
import datetime
from gmail.gmail_client import get_unread_messages, get_confirmation_replies
from db import get_email_by_id
from config import POLL_INTERVAL_SECONDS
from util.log import log
from util.env_var_validator import check_required_env_vars
from util.draft_save_notify import draft_save_notify
from util.fun import LyricPrinter
from handlers.confirmation_response_handler import ConfirmationResponseHandler
from models import EmailStatus


def process_incoming_emails():
    """Check unread Gmail, draft replies, notify via SMS."""
    unread_emails = get_unread_messages()
    for email_data in unread_emails:
        draft_save_notify(
            recipient=email_data['from'],
            subject=email_data['subject'],
            received_content=email_data['body'],
            message_id=email_data['message_id'],
            status=EmailStatus.PENDING,
        )

def poll_confirmation_inbox():
    """Poll second Gmail inbox for Y/N/R replies to confirmation requests."""
    while True:
        confirmations = get_confirmation_replies()  # Returns {email_id: (response, feedback)}
        for email_id, (response, feedback) in confirmations.items():
            log(f"email_id: {email_id}. raw response: {response}. raw feedback: {feedback}")
            email_record = get_email_by_id(email_id)
            
            if not email_record or email_record['status'] != EmailStatus.PENDING:
                continue
            
            response_handler = ConfirmationResponseHandler(email_id, response, feedback, email_record)
            response_handler.handle_response()

        time.sleep(POLL_INTERVAL_SECONDS)

def main():
    # Validate env vars
    log(f"Validating local environment variables.....")
    check_required_env_vars()
    
    # fun
    LyricPrinter([
        {
            "title": "Song title",
            "section": "Intro",
            "lyrics": None,
            "duration": datetime.timedelta(seconds=3)
        }
    ]).start()
    
    log('G M AI L  M O N I T O R I N G.....')
    
    # Start polling thread
    poll_thread = threading.Thread(target=poll_confirmation_inbox, daemon=True)
    poll_thread.start()

    # Main loop to check new emails every few minutes
    while True:
        process_incoming_emails()
        time.sleep(POLL_INTERVAL_SECONDS)

if __name__ == '__main__':
    main()
