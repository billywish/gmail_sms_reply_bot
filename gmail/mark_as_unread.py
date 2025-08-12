import imaplib
from config import GMAIL_APP_PASSWORD, GMAIL_USER
from util.log import log

def mark_email_as_unread(message_uid):
    log(f"Marking email {message_uid} as unread")
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    mail.uid('STORE', message_uid, '-FLAGS', '(\\Seen)')

