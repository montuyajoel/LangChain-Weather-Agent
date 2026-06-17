from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from main import app
from agents.weather_agent import ask_agent
from tools.tools import get_current_weather

client = TestClient(app)


# ==========================================================
# Health Check
# ==========================================================

def test_health_check():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


# ==========================================================
# Session Cookie
# ==========================================================

@patch("main.ask_agent")
def test_session_cookie_created(
    mock_ask_agent
):

    mock_ask_agent.return_value = (
        "Weather is sunny."
    )

    response = client.post(
        "/ask",
        json={
            "question": "Weather today?"
        }
    )

    assert response.status_code == 200

    assert "session_id" in response.cookies


# ==========================================================
# Weather Endpoint
# ==========================================================

@patch("main.ask_agent")
def test_weather_endpoint(
    mock_ask_agent
):

    mock_ask_agent.return_value = (
        "Yes, bring an umbrella."
    )

    response = client.post(
        "/ask",
        json={
            "question": "Will it rain tomorrow?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "response" in data

    assert (
        data["response"]
        == "Yes, bring an umbrella."
    )


# ==========================================================
# Agent Function
# ==========================================================

def test_ask_agent():

    mock_agent = Mock()

    mock_agent.invoke.return_value = {
        "messages": [
            {
                "content": "Sunny"
            }
        ]
    }

    result = ask_agent(
        mock_agent,
        "test-user",
        "Weather?"
    )
    assert result == "Sunny"


# ==========================================================
# Weather Tool
# ==========================================================

def test_weather_tool():

    result = get_current_weather.invoke(
        {
            "location": "Dublin"
        }
    )

    assert result is not None


# ==========================================================
# Conversation Memory
# ==========================================================

@patch("agents.weather_agent.ask_agent")
def test_memory_conversation(
    mock_ask_agent
):

    mock_ask_agent.side_effect = [
        (
            "For Dun Laoghaire tomorrow, "
            "the weather forecast is light drizzle."
        ),
        (
            "An umbrella may not be the most effective solution "
            "for this light drizzle."
        )
    ]

    first = mock_ask_agent(
        None,
        "user-1",
        "Weather in Dun Laoghaire tomorrow?"
    )

    second = mock_ask_agent(
        None,
        "user-1",
        "Will umbrella help?"
    )

    assert first

    assert second

    assert (
        "umbrella"
        in second.lower()
    )


# ==========================================================
# Actual Response Structure
# ==========================================================

@patch("main.ask_agent")
def test_response_structure(
    mock_ask_agent
):

    mock_ask_agent.return_value = (
        "Considering the light drizzle, "
        "indoor activities are recommended."
    )

    response = client.post(
        "/ask",
        json={
            "question": "What should I do tomorrow?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data["response"],
        str
    )

    assert len(
        data["response"]
    ) > 0
