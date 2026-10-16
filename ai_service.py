import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

client = Client(
    host=os.getenv("OLLAMA_HOST", "http://localhost:11434")
)

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

def generate_response(messages: list) -> str:
    result = client.chat(
        model=MODEL,
        messages=messages
    )
    return result["message"]["content"]