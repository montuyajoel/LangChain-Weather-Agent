from typing import Any, Dict

from langchain.tools import tool

from API.weather_api import fetch_current_weather, fetch_weather_forecast


@tool
def get_current_weather(location: str) -> Dict[str, Any]:
    """
    Get the current weather for a city or place.
    Use this when the user asks about the weather right now, current temperature,
    humidity, rain, wind, or outdoor comfort.
    """

    return fetch_current_weather(location)


@tool
def get_weather_forecast(location: str, days: int = 3) -> Dict[str, Any]:
    """
    Get the weather forecast for a city or place.
    Use this when the user asks about tomorrow, the next few days, weekend weather,
    rain probability, or planning around future weather.
    """

    return fetch_weather_forecast(location, days)