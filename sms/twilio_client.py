from twilio.rest import Client
from util.log import log
from config import (
    USER_PHONE,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER
)

# not currently in use
def send_sms_twilio(message, email_id=None):
    if not USER_PHONE:
        log("User phone number is not configured.")
        return
    
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
        log("Twilio configuration is incomplete.")
        return

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE
        )

        if email_id:
            log(f"SMS sent to {USER_PHONE} via Twilio. email_id: {email_id}, Twilio SID: {sms.sid}")
        else:
            log(f"SMS sent to {USER_PHONE} via Twilio. Twilio SID: {sms.sid}")

    except Exception as e:
        if email_id:
            log(f"Failed to send SMS to {USER_PHONE} via Twilio for email_id {email_id}: {e}")
        else:
            log(f"Failed to send SMS via Twilio: {e}")
            
        log('Attempting to send via SMTP')
        sms(message, email_id)