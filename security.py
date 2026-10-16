import hmac
import os
from dotenv import load_dotenv
from fastapi import Header, HTTPException

load_dotenv()

def verify_api_key(x_api_key: str = Header(default="")):
    expected = os.getenv("API_KEY", "")

    if not expected or not hmac.compare_digest(x_api_key, expected):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )