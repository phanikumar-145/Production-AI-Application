from fastapi import HTTPException

BLOCKED_TERMS = [
    "steal a password",
    "steal credentials",
    "make a bomb",
]

def validate_input(message: str) -> str:
    message = message.strip()

    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    if any(term in message.lower() for term in BLOCKED_TERMS):
        raise HTTPException(status_code=400, detail="Request blocked by safety policy")

    return message

def validate_output(reply: str) -> str:
    if not reply or not reply.strip():
        raise HTTPException(status_code=502, detail="AI returned an empty response")

    return reply.strip()