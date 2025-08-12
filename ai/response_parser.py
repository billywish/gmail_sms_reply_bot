import json
from ai.call_openai import call_openai

def parse_user_response_with_openai(user_text):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an assistant that reads user SMS replies and extracts the intent "
                "as one of these categories: YES, NO, REJECT, or INVALID. "
                "If REJECT, also extract optional feedback text."
            )
        },
        {
            "role": "user",
            "content": (
                f"User reply: {user_text}\n\n"
                "Respond with JSON like "
                "{\"intent\": \"YES\" | \"NO\" | \"REJECT\" | \"INVALID\", \"feedback\": \"optional text\"}"
            )
        }
    ]
    
    content = call_openai(messages)

    try:
        # Try to parse the JSON response
        parsed = json.loads(content)
        intent_enum_value = parsed.get("intent", "INVALID").upper()
        feedback_text = parsed.get("feedback", "")
    except json.JSONDecodeError:
        # If the response isn't valid JSON, fallback to INVALID intent
        intent_enum_value = "INVALID"
        feedback_text = ""

    return intent_enum_value, feedback_text