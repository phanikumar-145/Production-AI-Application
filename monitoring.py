from threading import Lock

_lock = Lock()

_metrics = {
    "requests": 0,
    "errors": 0,
    "total_response_seconds": 0.0,
}

def record_request():
    with _lock:
        _metrics["requests"] += 1

def record_error():
    with _lock:
        _metrics["errors"] += 1

def record_duration(seconds: float):
    with _lock:
        _metrics["total_response_seconds"] += round(seconds, 4)

def get_metrics() -> dict:
    with _lock:
        data = dict(_metrics)

    count = data["requests"]
    data["average_response_seconds"] = (
        round(data["total_response_seconds"] / count, 4)
        if count else 0.0
    )
    return data