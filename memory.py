from collections import defaultdict
from threading import Lock

MAX_MESSAGES = 20
_conversations = defaultdict(list)
_lock = Lock()

def get_history(session_id: str) -> list:
    with _lock:
        return list(_conversations[session_id])

def add_exchange(session_id: str, user_message: str, assistant_message: str):
    with _lock:
        history = _conversations[session_id]
        history.extend([
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": assistant_message},
        ])
        _conversations[session_id] = history[-MAX_MESSAGES:]

def clear_memory(session_id: str):
    with _lock:
        _conversations.pop(session_id, None)