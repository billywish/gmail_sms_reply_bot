import sys
import os
from util.log import log

def check_required_env_vars():
    required_vars = {
        'GMAIL_USER': 'Your Gmail email address used for sending emails',
        'GMAIL_APP_PASSWORD': 'App password for Gmail SMTP authentication',
        'CONFIRMATION_INBOX_USER': 'Email address for confirmation inbox used to send SMS',
        'CONFIRMATION_INBOX_PASSWORD': 'Password for confirmation inbox email account',
        'USER_PHONE': 'The phone number to receive SMS notifications',
        'USER_CARRIER': 'The mobile carrier for the SMS recipient (e.g., att, verizon)'    
        }

    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        log("ERROR: The following required environment variables are missing or empty:\n")
        for var in missing_vars:
            log(f"  - {var}: {required_vars[var]}")
        log("\nPlease set these variables in your .env file or environment before running the script.")
        sys.exit(1)