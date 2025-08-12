from sms.sms_client import send_sms

def send_reply_format_instructions():
    """
    Send SMS with clear, concise instructions about the expected reply format.
    """
    instructions = (
        "Please reply with:\n"
        "Y <ID> - to confirm and send the email\n"
        "N <ID> - to discard the email\n"
        "R <ID> <optional feedback> - to reject and provide feedback\n\n"
        "Example:\n"
        "Y 12345\n"
        "R 12345 too wordy"
    )
    send_sms(instructions)