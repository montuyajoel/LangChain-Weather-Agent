# LangChain Weather Agent

Production-ready weather assistant built with FastAPI, LangGraph, Open-Meteo, and configurable LLM providers (Ollama or OpenAI).

## Features

* Current weather conditions
* Multi-day forecasts
* Weather-based recommendations
* Short-term memory using LangGraph
* REST API
* OpenAI and Ollama support
* Weather guardrails
* GitHub Actions CI/CD

---

## Quick Start

### Clone Repository

```bash
git clone https://github.com/montuyajoel/LangChain-Weather-Agent.git
cd LangChain-Weather-Agent
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## LLM Configuration

Supported providers:

* Ollama
* OpenAI

Configure in `constants.py`:

```python
SET_MODEL_PROVIDER = "llama"
```

or

```python
SET_MODEL_PROVIDER = "openai"
```

### OpenAI Setup

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Recommended models:

```python
gpt-5-mini
gpt-5
gpt-5-nano
```

---

## Run Application

```bash
uvicorn main:app --reload
```

Available endpoints:

```text
http://localhost:8000
http://localhost:8000/docs
```

---

## API Example

### Request

```json
{
  "question": "Will it rain in Dublin tomorrow?"
}
```

### Response

```json
{
  "response": "Yes. Bring an umbrella. Rain is expected throughout the day."
}
```

---

## Version 2.0.0

### New Features

* Folder restructuring
* OpenAI (ChatGPT) support
* Configurable model provider
* Weather guardrails
* Token optimization
* Improved memory utilization

### Performance Improvements

Previous:

```text
3936 tokens
$0.002540
```

Current:

```text
2203 tokens
$0.002001
```

Improvement:

```text
44.03% token reduction
21.22% cost reduction
```

---

## Iterations

### v1.0.0

* Ollama support
* LangGraph memory
* Open-Meteo integration
* FastAPI API
* GitHub Actions CI

### v2.0.0

* OpenAI support
* Guardrails
* Folder restructuring
* Token optimization
* Improved response quality

---

## Tech Stack

| Tool           | Purpose             |
| -------------- | ------------------- |
| FastAPI        | REST API            |
| LangGraph      | Agent orchestration |
| LangChain      | Tool abstraction    |
| OpenAI         | Cloud LLM           |
| Ollama         | Local LLM           |
| Open-Meteo     | Weather data        |
| Pytest         | Testing             |
| GitHub Actions | CI/CD               |

---

## Attribution

Weather data provided by Open-Meteo under CC BY 4.0.

## License

For learning, experimentation, and AI agent development.
