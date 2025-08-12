from sms.sms_client import send_sms_in_chunks
from ai.writer import generate_email_draft, refine_email_draft
from db import save_email
from models import EmailStatus
from config import CUSTOMER_CONTEXT

def draft_save_notify(recipient, subject, received_content, message_id, current_draft=None, status=EmailStatus.PENDING):
    """
    Generate (or use existing) email draft, save it to DB, and notify user via SMS.
    
    Args:
        recipient (str): Email recipient address.
        subject (str): Email subject line.
        received_content (str): Original email body received.
        current_draft (str, optional): If provided, use this draft instead of generating a new one.
        status (EmailStatus or str): Status to save for the email record.
    
    Returns:
        int: The database ID of the saved email record.
    """
    if current_draft is None:
        generated_reply = generate_email_draft(subject, received_content, CUSTOMER_CONTEXT)
    else:
        generated_reply = current_draft

    email_id = save_email(recipient, subject, received_content, generated_reply, status=status, message_id=message_id)
    
    sms_message = f"Reply Y/N/R with ID {email_id}\nDraft for {recipient}:\n{generated_reply}"
    send_sms_in_chunks(sms_message, email_id)
    
    return email_id

def redraft_save_notify(email_record, feedback):
    """
    Refine an existing draft based on feedback, save it as a new pending draft,
    and notify the user via SMS with the new draft and ID.

    Args:
        email_record (dict or ORM object): Existing email data with keys:
            - 'recipient'
            - 'subject'
            - 'received_content'
            - 'generated_reply'
        feedback (str): User feedback to refine the draft.

    Returns:
        int: The database ID of the new saved draft email.
    """
    new_draft = refine_email_draft(
        email_record['subject'],
        email_record['received_content'],
        email_record['generated_reply'],
        feedback,
        CUSTOMER_CONTEXT
    )
    
    new_email_id = save_email(
        recipient=email_record['recipient'],
        subject=email_record['subject'],
        received_content=email_record['received_content'],
        generated_reply=new_draft,
        status=EmailStatus.PENDING,
        message_id=email_record['message_id']
    )
    
    sms_message = f"Reply Y/N/R with ID {new_email_id}\nDraft for {email_record['recipient']}:\n{new_draft}"
    send_sms_in_chunks(sms_message, new_email_id)
    
    return new_email_id