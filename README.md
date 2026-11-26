#  Production AI Application

A secure, modular, and production-oriented AI application built using **Python, FastAPI, and Ollama**. This project demonstrates how to integrate Large Language Models (LLMs) into an API with authentication, safety guardrails, conversational memory, logging, and performance monitoring.

##  Project Overview

Building an AI chatbot is relatively simple, but deploying an AI application in a production environment requires additional components such as security, input validation, error handling, conversation management, and monitoring.

The **Production AI Application** addresses these requirements by providing a modular backend architecture for serving AI-powered conversational responses through REST APIs.

The application integrates a locally hosted LLM through Ollama and exposes its capabilities through FastAPI endpoints.

It also implements API-key authentication, input and output validation, session-based conversation memory, structured logging, and basic performance metrics.

##  Project Objectives

- Build a production-oriented AI backend using FastAPI.
- Integrate locally hosted Large Language Models using Ollama.
- Implement API-key-based authentication.
- Apply input and output validation using guardrails.
- Maintain conversation context using session-based memory.
- Implement centralized logging and exception handling.
- Monitor API requests, errors, and response duration.
- Develop a modular and maintainable application architecture.
- Test important application components using Pytest.

##  Key Features

### 1. AI Integration
- Integrates Ollama with locally hosted LLMs.
- Generates AI-powered conversational responses.
- Supports configurable model selection.
- Maintains system instructions for assistant behavior.

### 2. API Security
- API-key-based authentication.
- Request authentication through HTTP headers.
- Secure API-key comparison using `hmac.compare_digest`.
- Protects sensitive API endpoints from unauthorized access.

### 3. AI Guardrails
- Validates incoming user messages.
- Blocks configured restricted phrases.
- Validates generated AI responses.
- Handles empty or invalid responses.

### 4. Conversational Memory
- Maintains conversation history using session IDs.
- Provides previous conversation context to the LLM.
- Limits stored conversation history to a maximum of 20 messages per session.
- Supports clearing conversation memory.

### 5. Logging and Monitoring
- Centralized application logging.
- Tracks total API requests.
- Tracks application errors.
- Measures response duration.
- Calculates average response time.
- Provides monitoring metrics through an API endpoint.

### 6. Error Handling
- Handles invalid requests.
- Returns appropriate HTTP status codes.
- Handles AI service failures.
- Logs unexpected application exceptions.

### 7. Automated Testing
- Includes a dedicated testing directory.
- Uses Pytest for automated testing.
- Uses HTTPX for API testing.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API development |
| Ollama | Local LLM integration |
| Llama 3.2 | Default configured language model |
| Pydantic | Request and response validation |
| Python-Dotenv | Environment variable management |
| Uvicorn | ASGI application server |
| Pytest | Automated testing |
| HTTPX | API testing |
| HMAC | Secure API-key comparison |

##  System Architecture

```text
              Client Application
                     |
                     v
                FastAPI Server
                     |
                     v
             API Key Authentication
                     |
                     v
               Input Guardrails
                     |
                     v
             Session-Based Memory
                     |
                     v
               AI Service Layer
                     |
                     v
                Ollama LLM
                     |
                     v
              AI Response
                     |
                     v
               Output Validation
                     |
                     v
             Return JSON Response
                     |
                     v
          Logging and Monitoring
```

##  Project Structure

```text
Production-AI-Application/
│
├── outputs/
│
├── tests/
│
├── ai_service.py
├── guardrails.py
├── logging_config.py
├── main.py
├── memory.py
├── monitoring.py
├── security.py
│
├── requirements.txt
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Main FastAPI application and API endpoints |
| `ai_service.py` | Connects to Ollama and generates AI responses |
| `security.py` | Implements API-key authentication |
| `guardrails.py` | Validates user inputs and AI outputs |
| `memory.py` | Manages session-based conversation history |
| `logging_config.py` | Configures application logging |
| `monitoring.py` | Tracks API requests, errors, and response times |
| `tests/` | Contains automated application tests |
| `outputs/` | Stores project-generated outputs |
| `requirements.txt` | Contains Python dependencies |

##  Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/phanikumar-145/Production-AI-Application.git
```

### 2. Navigate to the Project

```bash
cd Production-AI-Application
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install and Start Ollama

Download Ollama:

https://ollama.com/download

Pull the default configured model:

```bash
ollama pull llama3.2
```

Start the Ollama service if it is not already running:

```bash
ollama serve
```

### 7. Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following:

```env
API_KEY=your_secure_api_key
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

Replace `your_secure_api_key` with your own secure API key.

**Important:** Never upload your `.env` file or expose your API key on GitHub.

### 8. Run the Application

Open a terminal in the project directory and execute:

```bash
uvicorn main:app --reload
```

The FastAPI server will start at:

```text
http://127.0.0.1:8000
```

##  API Endpoints

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/health` | Checks application health | Not required |
| POST | `/chat` | Generates an AI response | Required |
| GET | `/metrics` | Retrieves application metrics | Required |
| DELETE | `/memory/{session_id}` | Clears session conversation history | Required |

### 1. Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### 2. AI Chat Endpoint

```http
POST /chat
```

Request headers:

```text
x-api-key: your_secure_api_key
```

Request body:

```json
{
  "message": "Explain machine learning",
  "session_id": "user_001"
}
```

Example response:

```json
{
  "reply": "Machine learning is a branch of artificial intelligence...",
  "session_id": "user_001"
}
```

### 3. Monitoring Endpoint

```http
GET /metrics
```

Provides information about:
- Total requests.
- Total errors.
- Total response duration.
- Average response time.

### 4. Clear Conversation Memory

```http
DELETE /memory/user_001
```

Clears the conversation history associated with the specified session.

##  API Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, open:

**Swagger UI:**

http://127.0.0.1:8000/docs

**ReDoc:**

http://127.0.0.1:8000/redoc

Use Swagger UI to test the API endpoints and provide the required API key for protected endpoints.

##  Testing

Run automated tests using:

```bash
pytest -v
```

The project includes a dedicated testing directory for validating application behavior.

##  Security Considerations

- API-key authentication for protected endpoints.
- Input validation before processing user messages.
- Output validation before returning AI responses.
- Environment variables for sensitive configuration.
- Restricted request length.
- Exception handling to avoid exposing internal error details.

**Note:** The current guardrails implement basic phrase-based filtering. They should not be considered a complete security or content-safety solution.

##  Real-World Applications

This architecture can be extended and used in:

- Enterprise AI assistants.
- Internal company chatbots.
- Customer support automation.
- AI-powered backend services.
- Knowledge-based conversational applications.
- Secure LLM-powered REST APIs.
- AI integration in existing business applications.

##  Future Enhancements

- Add persistent conversation storage using PostgreSQL.
- Implement Redis-based session management.
- Add advanced prompt injection protection.
- Integrate more sophisticated AI safety guardrails.
- Implement rate limiting and request throttling.
- Add role-based access control.
- Introduce Docker-based deployment.
- Add CI/CD automation using GitHub Actions.
- Integrate Prometheus and Grafana for advanced monitoring.
- Add cloud-based LLM provider support.
- Implement production-grade authentication and authorization.

##  Author

**Phani Kumar**

AI/ML & Generative AI Developer

- GitHub: https://github.com/phanikumar-145
- Project: https://github.com/phanikumar-145/Production-AI-Application

---

 If you find this project useful, consider giving it a star!

**Built with Python, FastAPI, Ollama, and Generative AI.**
