from util.log import log
from ai.call_openai import call_openai


def build_base_messages(subject, body, customer_context=None):
    system_content = (
        "You are a helpful assistant that drafts professional, concise, ready-to-send email replies. "
        "It’s okay to include greetings like 'Hi' or closings like 'Thanks,' but NEVER include placeholders "
        "like '[Your Name]', '[Recipient’s Name]', or any generic signatures."
    )
    if customer_context:
        system_content += f"\n\nAdditional customer context to guide your response:\n{customer_context}"

    user_content = (
        f"Subject: {subject}\n"
        f"Email body:\n{body}\n\n"
        f"Please write a clear, concise reply to this email."
    )

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]


def generate_email_draft(subject, body, customer_context=None):
    log('generating email draft...')
    messages = build_base_messages(subject, body, customer_context)
    return call_openai(messages, max_tokens=300)


def refine_email_draft(original_subject, original_body, current_draft, feedback, customer_context=None):
    log('refining email draft with feedback...')
    messages = build_base_messages(original_subject, original_body, customer_context)

    refinement_content = (
        f"Current Draft:\n{current_draft}\n\n"
        f"Feedback from user:\n{feedback}\n\n"
        "Please rewrite the draft incorporating the feedback. Keep it clear and concise."
    )

    messages.append({"role": "user", "content": refinement_content})

    return call_openai(messages)

