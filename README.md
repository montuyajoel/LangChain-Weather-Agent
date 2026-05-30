# LangChain Weather Agent

A simple weather agent built with **LangChain**, **Ollama**, and the **Open-Meteo API**.

The agent accepts natural-language weather questions such as:

```text
What is the weather in Dublin?
```

It extracts the location, calls a weather tool, fetches live weather data from Open-Meteo, and returns a readable weather response.

---

## Project Structure

```text
LangChain-Weather-Agent/
│
├── constants.py
├── weather_api.py
├── tools.py
├── main.py
├── requirements.txt
└── README.md
```

### File Purpose

| File               | Purpose                                                                     |
| ------------------ | --------------------------------------------------------------------------- |
| `constants.py`     | Stores API URLs, weather field names, model name, and weather code mappings |
| `weather_api.py`   | Handles geocoding and weather API requests                                  |
| `tools.py`         | Defines LangChain tools used by the agent                                   |
| `main.py`          | Builds and runs the LangChain weather agent                                 |
| `requirements.txt` | Lists required Python dependencies                                          |
| `README.md`        | Project setup and usage guide                                               |

---

## Prerequisites

Before running the project, install:

* Python 3.10 or higher
* Git
* Ollama

---

## 1. Install Ollama

### macOS

Install Ollama using Homebrew:

```bash
brew install ollama
```

Or install it from:

```text
https://ollama.com
```

After installation, verify that Ollama is available:

```bash
ollama --version
```

If the command works, Ollama is installed correctly.

---

## 2. Pull the Local Model

This project uses a free local model through Ollama.

Recommended model for MacBook Air M2 8GB:

```bash
ollama pull llama3.2:3b
```

Optional heavier model:

```bash
ollama pull llama3.1:8b
```

Use `llama3.2:3b` first because it is lighter and faster.

---

## 3. Start Ollama

Run:

```bash
ollama serve
```

Keep this terminal open while running the weather agent.

Open a second terminal tab for the next steps.

---

## 4. Clone the Repository

```bash
git clone https://github.com/montuyajoel/LangChain-Weather-Agent.git
```

Go inside the project folder:

```bash
cd LangChain-Weather-Agent
```

---

## 5. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## 6. Install Requirements

Install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Expected dependencies:

```text
langchain
langchain-ollama
langgraph
requests
```

---

## 7. Run the Weather Agent

```bash
python main.py
```

You should see:

```text
Weather Agent
Type 'exit' or 'quit' to stop.
```

---

## 8. Example Prompts

```text
What is the weather in Dublin?
```

```text
What is the current weather in Antipolo?
```

```text
Will it rain in Dublin tomorrow?
```

```text
Give me the 3-day forecast for Tokyo.
```

---

## How It Works

### Step 1: User asks a question

```text
What is the weather in Dublin?
```

### Step 2: LangChain agent reads the sentence

The agent identifies that the user is asking for current weather.

### Step 3: LangChain calls the weather tool

The agent calls:

```python
get_current_weather(location="Dublin")
```

### Step 4: The weather API converts the city into coordinates

```text
Dublin → latitude and longitude
```

### Step 5: Open-Meteo returns live weather data

The API returns data such as:

* Temperature
* Apparent temperature
* Humidity
* Precipitation
* Wind speed
* Weather condition

### Step 6: The agent returns a natural-language answer

Example:

```text
The current weather in Dublin, Ireland is overcast. The temperature is 16°C, feeling like 15°C. Humidity is 75%, precipitation is 0 mm, and wind speed is 14 km/h.
```

---

## Main Components

### `constants.py`

Stores reusable constants:

* Open-Meteo API URLs
* Weather fields
* Default Ollama model
* Weather code mapping

### `weather_api.py`

Handles direct API work:

* Converts location names into coordinates
* Fetches current weather
* Fetches forecast data
* Formats API output into dictionaries

### `tools.py`

Defines LangChain tools:

```python
get_current_weather
get_weather_forecast
```

These tools are exposed to the agent.

### `main.py`

Builds the agent using:

* `ChatOllama`
* LangChain `create_agent`
* Weather tools

It also handles the terminal input loop.

---

## Troubleshooting

### `zsh: command not found: ollama`

Ollama is not installed or not available in your PATH.

Fix:

```bash
brew install ollama
```

Then verify:

```bash
ollama --version
```

---

### `connection refused` or Ollama not responding

Ollama is not running.

Fix:

```bash
ollama serve
```

Keep the terminal open.

---

### Model not found

The model has not been downloaded.

Fix:

```bash
ollama pull llama3.2:3b
```

---

### Python package error

Dependencies are missing.

Fix:

```bash
pip install -r requirements.txt
```

---

### No location found

The location name may be unclear.

Use a more specific location:

```text
Dublin, Ireland
```

Instead of:

```text
Dublin
```

---

## Git Commands

Check project status:

```bash
git status
```

Add changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Update weather agent"
```

Push changes:

```bash
git push origin main
```

---

## Tech Stack

| Tool             | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Core programming language      |
| LangChain        | Agent framework                |
| LangChain Ollama | Local LLM integration          |
| Ollama           | Runs the local language model  |
| Open-Meteo       | Free weather and geocoding API |
| Requests         | HTTP API requests              |

---

## License

This project is for learning and experimentation.

## API Usage and Attribution

This project uses the **Open-Meteo API** for geocoding and weather forecast data.

Open-Meteo provides free API access for non-commercial use. The free API is rate-limited to **10,000 calls per day**, **5,000 calls per hour**, and **600 calls per minute**. Commercial use requires a paid customer API plan. Open-Meteo API data is provided under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

Required attribution:

```text
Weather data by Open-Meteo.com
