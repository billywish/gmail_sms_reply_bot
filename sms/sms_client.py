import time
import smtplib
from email.mime.text import MIMEText
from config import (
    USER_PHONE,
    USER_CARRIER,
    CONFIRMATION_INBOX_USER,
    CONFIRMATION_INBOX_PASSWORD,
    SMTP_PORT,
    SMTP_SERVER
)
from util.log import log


def send_sms_in_chunks(message, email_id=None):
    if not USER_PHONE or not USER_CARRIER:
        log("Phone or carrier not configured.")
        return
    
    SMS_CARRIERS = {
        'att': '@txt.att.net',
        'tmobile': '@tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@messaging.sprintpcs.com',
    }
    
    carrier_domain = SMS_CARRIERS.get(USER_CARRIER)
    if not carrier_domain:
        log(f"Unsupported carrier: {USER_CARRIER}")
        return
    
    to_number = f"{USER_PHONE}{carrier_domain}"

    # Calculate max chunk length considering prefix length
    total_chunks = (len(message) // 153) + 1  # rough estimate for prefix length 7
    max_chunk_length = 160 - len(f"({total_chunks}/{total_chunks}) ")  # dynamic prefix length

    # Split message into chunks considering prefix length
    chunks = []
    start = 0
    while start < len(message):
        chunk = message[start:start + max_chunk_length]
        chunks.append(chunk)
        start += max_chunk_length

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(CONFIRMATION_INBOX_USER, CONFIRMATION_INBOX_PASSWORD)

            for idx, chunk in enumerate(chunks, start=1):
                prefix = f"({idx}/{len(chunks)}) "
                formatted_chunk = prefix + chunk
                
                msg = MIMEText(formatted_chunk)
                msg['From'] = CONFIRMATION_INBOX_USER
                msg['To'] = to_number

                server.sendmail(CONFIRMATION_INBOX_USER, to_number, msg.as_string())
                time.sleep(1.5) # hopefully prevents throttling
                
                if email_id:
                    log(f"SMS part {idx}/{len(chunks)} sent to {to_number}. email_id: {email_id}")
                else:
                    log(f"SMS part {idx}/{len(chunks)} sent to {to_number}")

    except Exception as e:
        log(f"Failed to send SMS in chunks via SMTP: {e}")

        

def send_sms(message, email_id=None):
    if not USER_PHONE or not USER_CARRIER:
        log("Phone or carrier not configured.")
        return
    
    # Default SMS and MMS gateways
    SMS_CARRIERS = {
        'att': '@txt.att.net',
        'tmobile': '@tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@messaging.sprintpcs.com',
    }
    MMS_CARRIERS = {
        'att': '@mms.att.net',
        'tmobile': '@tmomail.net',
        'verizon': '@vzwpix.com',
        'sprint': '@pm.sprint.com',
    }
    
    using_sms = len(message) <= 160

    # Choose SMS or MMS based on message length
    if using_sms:
        carrier_domain = SMS_CARRIERS.get(USER_CARRIER)
    else:
        carrier_domain = MMS_CARRIERS.get(USER_CARRIER)
    
    if not carrier_domain:
        log(f"Unsupported carrier: {USER_CARRIER}")
        return

    to_number = f"{USER_PHONE}{carrier_domain}"
    msg = MIMEText(message)
    msg['From'] = CONFIRMATION_INBOX_USER
    msg['To'] = to_number

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(CONFIRMATION_INBOX_USER, CONFIRMATION_INBOX_PASSWORD)
            server.sendmail(CONFIRMATION_INBOX_USER, to_number, msg.as_string())

        if email_id:
            log(f"{'SMS' if using_sms else 'MMS'} sent to {to_number}. email_id: {email_id}")
        else:
            log(f"{'SMS' if using_sms else 'MMS'} sent to {to_number}")
            
    except Exception as e:
        log(f"Failed to send SMS via SMTP: {e}")

