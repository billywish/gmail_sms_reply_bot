import email
import imaplib
from config import (
    GMAIL_USER, GMAIL_APP_PASSWORD,
    CONFIRMATION_INBOX_USER, CONFIRMATION_INBOX_PASSWORD
)
from util.log import log

def _safe_decode(payload, charset='utf-8'):
    """Decode email payload with fallback to ISO-8859-1 and replace errors."""
    try:
        return payload.decode(charset)
    except (UnicodeDecodeError, LookupError):
        return payload.decode('ISO-8859-1', errors='replace')

def _fetch_unread_emails(username, password, process_msg_func):
    """Generic IMAP unread email fetcher with safe decoding."""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    typ, data = mail.search(None, '(UNSEEN)')
    results = []

    for num in data[0].split():
        typ, msg_data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        results.append(process_msg_func(msg))

    mail.logout()
    return results

def get_unread_messages():
    """Fetch unread messages from primary Gmail inbox."""
    def process_msg(msg):
        sender = email.utils.parseaddr(msg['From'])[1]
        subject = msg['Subject']
        message_id = msg['Message-ID']
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    payload = part.get_payload(decode=True)
                    charset = part.get_content_charset() or 'utf-8'
                    body = _safe_decode(payload, charset)
                    break
        else:
            payload = msg.get_payload(decode=True)
            charset = msg.get_content_charset() or 'utf-8'
            body = _safe_decode(payload, charset)

        return {
            'from': sender,
            'subject': subject,
            'body': body,
            'message_id': message_id
        }

    messages = _fetch_unread_emails(GMAIL_USER, GMAIL_APP_PASSWORD, process_msg)
    if messages:
        log(f"user inbox: {messages}")
    return messages

def get_confirmation_replies():
    """Poll second inbox for Y/N replies with tags. Return dict email_id->response."""
    def process_msg(msg):
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    payload = part.get_payload(decode=True)
                    charset = part.get_content_charset() or 'utf-8'
                    body = _safe_decode(payload, charset)
                    break
        else:
            payload = msg.get_payload(decode=True)
            charset = msg.get_content_charset() or 'utf-8'
            body = _safe_decode(payload, charset)

        parts = body.strip().split(maxsplit=2)  # allow feedback to be the 3rd element
        if len(parts) >= 2:
            resp, email_id = parts[0].lower(), parts[1]
            feedback = parts[2] if len(parts) > 2 else None
            if resp in ('y', 'n', 'r'):
                return (email_id, resp, feedback)
        return None

    processed = _fetch_unread_emails(
        CONFIRMATION_INBOX_USER, CONFIRMATION_INBOX_PASSWORD, process_msg
    )
    filtered = [item for item in processed if item is not None]
    if filtered:
        log(f"confirmation inbox: {filtered}")
    return {email_id: (resp, feedback) for email_id, resp, feedback in filtered if email_id}
