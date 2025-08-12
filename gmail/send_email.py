import smtplib
from email.mime.text import MIMEText
from config import GMAIL_USER, GMAIL_APP_PASSWORD, SMTP_SERVER, SMTP_PORT


def send_email(recipient, content, original_message_id=None):
    """
    Send an email via Gmail SMTP with optional threading headers.

    Args:
        recipient (str): Email recipient address.
        content (str): Email content, optionally starting with 'Subject:' line.
        original_message_id (str, optional): Message-ID of original email to reply in thread.
    """
    if content.startswith("Subject:"):
        subject_line, body = content.split("\n\n", 1)
        subject = subject_line.replace("Subject:", "").strip()
    else:
        subject = "No Subject"
        body = content

    msg = MIMEText(body, "plain")
    msg["From"] = GMAIL_USER
    msg["To"] = recipient
    msg["Subject"] = subject

    if original_message_id:
        msg["In-Reply-To"] = original_message_id
        msg["References"] = original_message_id

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_USER, recipient, msg.as_string())
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Error sending email: {e}")
