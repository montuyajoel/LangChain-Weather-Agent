# LangChain Weather Agent

A production-ready weather assistant built with:

* FastAPI
* LangGraph
* Ollama
* Open-Meteo API
* GitHub Actions

The assistant supports:

* Current weather lookups
* Multi-day forecasts
* Follow-up weather conversations
* Short-term memory using LangGraph
* REST API access
* Automated testing and CI/CD validation

---

# Features

## Weather Intelligence

Supports natural-language questions:

```text
What is the weather in Dublin?
```

```text
Will it rain tomorrow in Antipolo?
```

```text
Do I need an umbrella tomorrow?
```

```text
Should I wear a jacket?
```

---

## LangGraph Memory

Supports short-term conversation memory.

Example:

```text
User:
What is the weather in Dun Laoghaire tomorrow?

Assistant:
Light drizzle. High 15.5°C. Rain probability 98%.

User:
Will umbrella help?

Assistant:
Yes. Bring an umbrella. Rain probability is very high.
```

The assistant remembers previously discussed forecasts through LangGraph thread memory.

---

## FastAPI API

Expose the assistant through a REST API.

---

## GitHub Actions

Every Pull Request automatically runs:

* Linting
* Tests
* Coverage
* Docker build validation

PRs can be blocked from merging unless all checks pass.

---

# Project Structure

```text
LangChain-Weather-Agent/
│
├── app.py
├── agent.py
├── constants.py
├── weather_api.py
├── tools.py
│
├── prompts/
│   └── system_prompt.md
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       └── pr-validation.yml
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# File Purpose

| File              | Purpose                    |
| ----------------- | -------------------------- |
| app.py            | FastAPI REST API           |
| agent.py          | LangGraph weather agent    |
| weather_api.py    | Open-Meteo API integration |
| tools.py          | LangChain tools            |
| constants.py      | Project constants          |
| system_prompt.md  | Agent instructions         |
| test_app.py       | Automated tests            |
| pr-validation.yml | GitHub Actions workflow    |

---

# Prerequisites

Install:

* Python 3.11+
* Git
* Ollama

---

# Install Ollama

macOS:

```bash
brew install ollama
```

or

```text
https://ollama.com
```

Verify:

```bash
ollama --version
```

---

# Pull Model

Recommended:

```bash
ollama pull llama3.2:3b
```

Alternative:

```bash
ollama pull llama3.1:8b
```

---

# Start Ollama

```bash
ollama serve
```

Keep running.

---

# Clone Repository

```bash
git clone https://github.com/montuyajoel/LangChain-Weather-Agent.git
```

```bash
cd LangChain-Weather-Agent
```

---

# Create Virtual Environment

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Expected dependencies:

```text
fastapi
uvicorn
langchain
langchain-ollama
langgraph
requests
pytest
pytest-cov
httpx
```

---

# Run FastAPI

```bash
uvicorn app:app --reload
```

Server:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# REST API

## Health Check

Request:

```http
GET /
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Weather Question

Request:

```http
POST /ask
```

Body:

```json
{
  "question": "Will it rain in Dublin tomorrow?"
}
```

Response:

```json
{
  "response": "Yes. Bring an umbrella. Rain probability is high."
}
```

---

# LangGraph Integration

This project uses LangGraph to orchestrate the weather assistant.

Components:

* ChatOllama
* LangGraph ReAct Agent
* Open-Meteo Tools
* MemorySaver Checkpointer

Benefits:

* Tool orchestration
* Conversation memory
* Thread management
* Production-ready architecture

---

# Short-Term Memory

The assistant maintains conversation context.

Example:

```text
User:
Weather in Dublin tomorrow?

Assistant:
Forecast returned.

User:
Will umbrella help?

Assistant:
Uses the previous forecast to answer.
```

Current implementation:

```text
LangGraph MemorySaver
```

Future upgrade options:

```text
PostgreSQL Checkpointer
Redis Checkpointer
```

---

# How It Works

### Step 1

User asks:

```text
What is the weather in Dublin?
```

### Step 2

LangGraph agent evaluates the request.

### Step 3

Weather tool is selected.

### Step 4

Location is geocoded.

### Step 5

Open-Meteo returns weather data.

### Step 6

The agent generates a weather response.

### Step 7

LangGraph stores conversation state.

### Step 8

Future questions reuse previous weather context.

---

# Testing

Run tests:

```bash
python -m pytest tests/test_app.py -v
```

Coverage:

```bash
python -m pytest \
tests/test_app.py \
--cov=. \
--cov-report=term
```

Coverage areas:

* FastAPI endpoints
* Session middleware
* Agent execution
* LangGraph memory flow
* Weather tools

---

# GitHub Actions

The project includes CI validation.

Workflow:

```text
.github/workflows/pr-validation.yml
```

Process:

```text
Pull Request
    ↓
Install Dependencies
    ↓
Lint
    ↓
Tests
    ↓
Coverage
    ↓
Docker Build
    ↓
Pass / Fail
```

Branch protection can require successful completion before merge.

---

# Example Questions

```text
What is the weather in Dublin?
```

```text
Will it rain tomorrow in Antipolo?
```

```text
Do I need an umbrella tomorrow?
```

```text
Should I wear a jacket?
```

```text
Is it good weather for walking?
```

```text
Can I go cycling tomorrow?
```

---

# Troubleshooting

## Ollama Not Running

```bash
ollama serve
```

---

## Model Not Found

```bash
ollama pull llama3.2:3b
```

---

## Dependency Issues

```bash
pip install -r requirements.txt
```

---

## API Not Responding

Verify:

```bash
uvicorn app:app --reload
```

---

# Git Commands

Status:

```bash
git status
```

Stage:

```bash
git add .
```

Commit:

```bash
git commit -m "Update weather agent"
```

Push:

```bash
git push origin main
```

---

# Tech Stack

| Tool           | Purpose                        |
| -------------- | ------------------------------ |
| Python         | Core language                  |
| FastAPI        | REST API                       |
| LangGraph      | Agent orchestration and memory |
| LangChain      | Tool abstraction               |
| Ollama         | Local LLM runtime              |
| Open-Meteo     | Weather provider               |
| Requests       | API communication              |
| Pytest         | Testing                        |
| GitHub Actions | CI/CD                          |

---

# API Usage and Attribution

This project uses Open-Meteo for geocoding and weather forecast data.

Required attribution:

```text
Weather data by Open-Meteo.com
```

Open-Meteo data is provided under:

```text
CC BY 4.0
```

For commercial usage, review Open-Meteo licensing and API limits.

---

# License

This project is intended for learning, experimentation, and local AI agent development.
