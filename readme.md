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

# Setup Guide

This guide walks you through the basic steps to get the project running.

---

## 1. Clone or Download the Project

If you haven't already:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

## 2. Create a Python Virtual Environment

Isolate dependencies to avoid conflicts:

```bash
python3 -m venv venv
```

Activate it:

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

- **Windows (PowerShell):**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

---

## 3. Install Dependencies

Make sure you have a `requirements.txt` file in your project root (if not, see notes below).

Install packages with:

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in your project root and add your config:

```env
GMAIL_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password

CONFIRMATION_INBOX_USER=confirmation-inbox-email@gmail.com
CONFIRMATION_INBOX_PASSWORD=confirmation-inbox-app-password

USER_PHONE=1234567890
USER_CARRIER=verizon

POLL_INTERVAL_SECONDS=60

CUSTOMER_CONTEXT="Relevant customer info, policies, FAQs, etc."

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
```

> **Note:** For Gmail SMTP, use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) instead of your regular password.

---

## 5. Run Database Migrations (If Applicable)

If your project uses a database and migration system, run:

```bash
alembic upgrade head
```

*Skip if not using migrations.*

---

## 6. Run the Application

Start the main script:

```bash
python app.py
```

You should see logs confirming the bot is running and polling.

---

## 7. Using the Bot

- The bot polls emails every `POLL_INTERVAL_SECONDS` (default 60 seconds).
- Drafts replies using OpenAI and sends SMS notifications.
- Reply via SMS with:
  - `Y` (Yes) to send
  - `N` (No) to discard
  - `R` (Reject + feedback) to request revision

---

