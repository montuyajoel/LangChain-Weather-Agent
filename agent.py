from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from constants import DEFAULT_MODEL
from tools import get_current_weather, get_weather_forecast


def build_weather_agent():
    """
    Compose the model and tools into one LangChain weather agent.
    """

    model = ChatOllama(
        model=DEFAULT_MODEL,
        temperature=0,
    )

    agent = create_agent(
        model=model,
        tools=[
            get_current_weather,
            get_weather_forecast,
        ],
        system_prompt=(
            "You are a practical weather assistant. "
            "Use get_current_weather for current weather questions. "
            "Use get_weather_forecast for forecast, tomorrow, weekend, or planning questions. "
            "Answer directly. Include Celsius temperature, apparent temperature, humidity, "
            "precipitation, wind, and condition when available."
        ),
    )

    return agent


def ask_agent(agent, question: str) -> str:
    """
    Send a user question to the agent and return the final response.
    """

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    return result["messages"][-1].content


def main():
    agent = build_weather_agent()

    print("Weather Agent")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        question = input("\nAsk: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        try:
            answer = ask_agent(agent, question)
            print("\nAgent:", answer)

        except Exception as error:
            print("\nError:", error)


if __name__ == "__main__":
    main()