import os
from dotenv import load_dotenv

load_dotenv()

# primary inbox being monitored
GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

# secondary inbox for text confirmations
CONFIRMATION_INBOX_USER = os.getenv('CONFIRMATION_INBOX_USER')
CONFIRMATION_INBOX_PASSWORD = os.getenv('CONFIRMATION_INBOX_PASSWORD')

# user phone info for draft review
USER_PHONE = os.getenv('USER_PHONE')
USER_CARRIER = os.getenv('USER_CARRIER')

# how frequently to monitor the inbox
POLL_INTERVAL_SECONDS = int(os.getenv('POLL_INTERVAL_SECONDS', 60))

# custom string that's added to each prompt send to open ai
CUSTOMER_CONTEXT = os.getenv('CUSTOMER_CONTEXT')

# twilio (text service) creds
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


