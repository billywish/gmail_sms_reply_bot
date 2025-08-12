from openai import OpenAI
import os
from util.log import log

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")


def call_openai(messages, max_tokens=400, temperature=0.7):
    """
    Internal helper to call the OpenAI Chat API and return the trimmed content.
    Backwards compatible with old and new API parameter names/limits.
    """
    params = {
        "model": OPENAI_MODEL,
        "messages": messages,
    }

    # New token param logic
    if OPENAI_MODEL.startswith(("gpt-4o", "gpt-5")):
        params["max_completion_tokens"] = max_tokens
    else:
        params["max_tokens"] = max_tokens

    # Temperature logic (skip if model only supports default=1)
    if not (OPENAI_MODEL.startswith("gpt-5") and temperature != 1):
        params["temperature"] = temperature

    response = client.chat.completions.create(**params)

    log(f"response.usage.total_tokens: {response.usage.total_tokens}")
    content = response.choices[0].message.content.strip()
    log(f"Generated content using model, {OPENAI_MODEL}: {content}")
    return content