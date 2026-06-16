import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from constants import DEFAULT_MODEL_LLAMA, DEFAULT_MODEL_OPENAI, SET_MODEL_PROVIDER
from tools.tools import get_current_weather, get_weather_forecast
from tools.token_usage import get_billable_tokens, get_estimated_cost
from pathlib import Path

# Load environment variables from .env file
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

# Check if the OPENAI_API_KEY is set and valid
if not api_key:
    print("Warning: OPENAI_API_KEY is not set. OpenAI models will not work.")
elif not api_key.startswith("sk-proj-"):
    print("Warning: OPENAI_API_KEY is not in the correct format.")
    print("Ollama will be employed as the default model provider.")
elif api_key.strip() != api_key:
    print("Warning: OPENAI_API_KEY has leading or trailing whitespace.")
    print("Ollama will be employed as the default model provider.")
else:
    print("OPENAI_API_KEY is set correctly.")

# Set the model provider based on the configuration
if SET_MODEL_PROVIDER == "openai" and api_key:
    MODEL_PROVIDER = ChatOpenAI
    DEFAULT_MODEL = DEFAULT_MODEL_OPENAI
    print(f"Using OpenAI model: {DEFAULT_MODEL}")
else :
    MODEL_PROVIDER = ChatOllama
    DEFAULT_MODEL = DEFAULT_MODEL_LLAMA
    print(f"Using LLaMA model: {DEFAULT_MODEL}")


SYSTEM_PROMPT = Path("prompts/system_prompt.md").read_text()

def build_weather_agent():
    """
    Compose the model and tools into one LangChain weather agent.
    """

    model = MODEL_PROVIDER(
        model=DEFAULT_MODEL,
        temperature=0,
    )

    memory = MemorySaver()

    agent = create_agent(
        model=model,
        tools=[
            get_current_weather,
            get_weather_forecast,
        ],
        checkpointer=memory,
        system_prompt=SYSTEM_PROMPT,
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

    # Get the messages from the result
    messages = result.get("messages", [])

    # Calculate the total tokens used and estimated cost
    total_tokens = get_billable_tokens(result).get("total_tokens")
    estimated_cost = get_estimated_cost(result)
   
    print(f"Total tokens used: {total_tokens} Estimated cost: {estimated_cost}.")
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