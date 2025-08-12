# Email Drafting and SMS Notification System

This project automates email reply drafting and notification via SMS, incorporating customer-specific context for better personalized responses.

---

## Features

- **Automated Draft Generation:** Generates email drafts using OpenAI based on the original email content and additional customer context.
- **Draft Refinement:** Refines drafts based on user feedback to improve clarity and accuracy.
- **SMS Notifications:** Sends SMS to users with draft previews and instructions to reply with Y/N/R (Yes/No/Reject) along with the draft ID.
- **Threaded Email Replies:** Maintains email threading by referencing original message IDs.
- **Persistent Storage:** Saves emails and drafts in a database with status tracking.

---

## Environment Variables / Config

Add the following environment variables to your `.env` file or system environment for proper configuration:

```bash
GMAIL_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password

CONFIRMATION_INBOX_USER=confirmation-inbox-email@gmail.com
CONFIRMATION_INBOX_PASSWORD=confirmation-inbox-app-password

USER_PHONE=your-phone-number
USER_CARRIER=your-phone-carrier

POLL_INTERVAL_SECONDS=60

CUSTOMER_CONTEXT="Insert relevant details about your customer, website, FAQs, policies, etc. This context will be used to improve draft relevance."
```

- `GMAIL_USER` and `GMAIL_APP_PASSWORD`: Credentials for sending emails via Gmail SMTP.
- `CONFIRMATION_INBOX_USER` and `CONFIRMATION_INBOX_PASSWORD`: Credentials for the inbox that receives SMS replies forwarded as emails.
- `USER_PHONE` and `USER_CARRIER`: The phone number (with no spaces, dashes or country code) and the carrier (eg verizon) used to send SMS notifications.
- `POLL_INTERVAL_SECONDS`: How often (in seconds) the system polls for new emails and replies. Default is 60 seconds.
- `CUSTOMER_CONTEXT`: A string containing customer-specific information to help the AI generate better email drafts.

---

## Usage

### `draft_save_notify`

Generates a new draft (or uses an existing draft), saves it to the database, and sends an SMS with the draft and instructions.

```python
draft_save_notify(
    recipient="user@example.com",
    subject="Inquiry about service",
    received_content="Original email body here",
    message_id="<original-email-message-id>"
)
```

### `redraft_save_notify`

Refines an existing draft based on user feedback, saves it as a new pending draft, and sends an updated SMS notification.

```python
redraft_save_notify(email_record, feedback="Please clarify the refund policy.")
```

---

## Prompt Customization with Customer Context

Your OpenAI prompts now include `CUSTOMER_CONTEXT` to give the AI relevant background information about the customer’s business, FAQs, or policies. This helps produce replies that are more accurate and aligned with customer specifics.

---

## Example SMS Notification

```
Reply Y/N/R with ID 123
Draft for user@example.com:
Thank you for reaching out. Our refund policy allows returns within 30 days...
```

---

## Notes

- The system expects SMS replies in Y/N/R format with optional feedback after an 'R'.
- The email threading is maintained by passing and storing the original email’s message ID.

---

## Setup

1. Install dependencies.
2. Configure your environment variables including Gmail credentials and `CUSTOMER_CONTEXT`.
3. Run the polling service that checks for incoming emails, drafts replies, and sends SMS notifications.
4. Reply via SMS with your decision (Y/N/R) and feedback if applicable.

---

