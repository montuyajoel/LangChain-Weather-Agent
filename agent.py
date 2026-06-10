from unittest import result

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama

from constants import DEFAULT_MODEL
from tools import get_current_weather, get_weather_forecast

from pathlib import Path

SYSTEM_PROMPT = Path("prompts/system_prompt.md").read_text()

def build_weather_agent():
    """
    Compose the model and tools into one LangChain weather agent.
    """

    model = ChatOllama(
        model=DEFAULT_MODEL,
        temperature=0,
    )

    memory = MemorySaver()

    agent = create_react_agent(
        model=model,
        tools=[
            get_current_weather,
            get_weather_forecast,
        ],
        checkpointer=memory,
        prompt=SYSTEM_PROMPT,
    )

    return agent



def ask_agent(
    agent,
    session_id: str,
    question: str
):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": session_id
            }
        }
    )

    messages = result.get("messages", [])

    if not messages:
        return "No response generated."

    last_message = messages[-1]

    # LangGraph AIMessage
    if hasattr(last_message, "content"):
        return last_message.content

    # Mocked dictionary
    if isinstance(last_message, dict):
        return last_message.get(
            "content",
            ""
        )

    return str(last_message)