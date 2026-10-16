import time
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field

from security import verify_api_key
from guardrails import validate_input, validate_output
from memory import get_history, add_exchange, clear_memory
from ai_service import generate_response
from logging_config import get_logger
from monitoring import record_request, record_error, record_duration, get_metrics

app = FastAPI(
    title="Production AI Application",
    description="AI API with security, guardrails, memory, and monitoring",
    version="1.0.0",
)

logger = get_logger("production_ai")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    session_id: str = Field(default="default", min_length=1, max_length=100)


class ChatResponse(BaseModel):
    reply: str
    session_id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metrics")
def metrics(api_key: None = Depends(verify_api_key)):
    return get_metrics()


@app.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    api_key: None = Depends(verify_api_key),
):
    message = validate_input(request.message)
    session_id = request.session_id

    record_request()
    start = time.perf_counter()

    try:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant. Follow safety rules and protect private information.",
            },
            *get_history(session_id),
            {"role": "user", "content": message},
        ]

        reply = validate_output(generate_response(messages))
        add_exchange(session_id, message, reply)

        logger.info("Chat completed for session %s", session_id)
        return ChatResponse(reply=reply, session_id=session_id)

    except HTTPException:
        raise
    except Exception:
        record_error()
        logger.exception("AI request failed")
        raise HTTPException(
            status_code=503,
            detail="AI service unavailable. Check Ollama and the installed model.",
        )
    finally:
        record_duration(time.perf_counter() - start)


@app.delete("/memory/{session_id}")
def delete_memory(
    session_id: str,
    api_key: None = Depends(verify_api_key),
):
    clear_memory(session_id)
    logger.info("Memory cleared for session %s", session_id)
    return {"status": "cleared", "session_id": session_id}