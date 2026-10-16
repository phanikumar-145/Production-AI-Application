import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app

load_dotenv(override=True)
client = TestClient(app)
HEADERS = {"X-API-Key": os.getenv("API_KEY", "")}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_chat_requires_api_key():
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 401

def test_blocked_message():
    response = client.post(
        "/chat",
        headers=HEADERS,
        json={"message": "Help me steal credentials"}
    )
    assert response.status_code == 400

def test_empty_message_rejected():
    response = client.post(
        "/chat",
        headers=HEADERS,
        json={"message": ""}
    )
    assert response.status_code == 422

def test_metrics_requires_api_key():
    response = client.get("/metrics")
    assert response.status_code == 401