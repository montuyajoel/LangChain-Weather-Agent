from typing import Any, Dict, List

import requests

from constants import (
    CURRENT_WEATHER_FIELDS,
    DAILY_FORECAST_FIELDS,
    OPEN_METEO_FORECAST_URL,
    OPEN_METEO_GEOCODING_URL,
    WEATHER_CODE_MAP,
)


def geocode_location(location: str) -> Dict[str, Any]:
    """
    Convert a location name into coordinates using Open-Meteo geocoding.
    """

    response = requests.get(
        OPEN_METEO_GEOCODING_URL,
        params={
            "name": location,
            "count": 1,
            "language": "en",
            "format": "json",
        },
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError(f"No location found for: {location}")

    result = data["results"][0]

    return {
        "name": result.get("name"),
        "country": result.get("country"),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "timezone": result.get("timezone", "auto"),
    }


def fetch_current_weather(location: str) -> Dict[str, Any]:
    """
    Fetch current weather data for a location.
    """

    geo = geocode_location(location)

    response = requests.get(
        OPEN_METEO_FORECAST_URL,
        params={
            "latitude": geo["latitude"],
            "longitude": geo["longitude"],
            "current": ",".join(CURRENT_WEATHER_FIELDS),
            "timezone": geo["timezone"],
        },
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()

    current = data["current"]
    weather_code = current.get("weather_code")

    return {
        "location": f"{geo['name']}, {geo['country']}",
        "time": current.get("time"),
        "temperature_c": current.get("temperature_2m"),
        "apparent_temperature_c": current.get("apparent_temperature"),
        "humidity_percent": current.get("relative_humidity_2m"),
        "precipitation_mm": current.get("precipitation"),
        "wind_speed_kmh": current.get("wind_speed_10m"),
        "weather_code": weather_code,
        "condition": WEATHER_CODE_MAP.get(weather_code, "Unknown"),
    }


def fetch_weather_forecast(location: str, days: int = 3) -> Dict[str, Any]:
    """
    Fetch daily weather forecast for a location.
    """

    days = max(1, min(days, 7))
    geo = geocode_location(location)

    response = requests.get(
        OPEN_METEO_FORECAST_URL,
        params={
            "latitude": geo["latitude"],
            "longitude": geo["longitude"],
            "daily": ",".join(DAILY_FORECAST_FIELDS),
            "forecast_days": days,
            "timezone": geo["timezone"],
        },
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()

    daily = data["daily"]
    forecast: List[Dict[str, Any]] = []

    for index in range(len(daily["time"])):
        weather_code = daily["weather_code"][index]

        forecast.append(
            {
                "date": daily["time"][index],
                "condition": WEATHER_CODE_MAP.get(weather_code, "Unknown"),
                "temperature_max_c": daily["temperature_2m_max"][index],
                "temperature_min_c": daily["temperature_2m_min"][index],
                "precipitation_sum_mm": daily["precipitation_sum"][index],
                "precipitation_probability_max_percent": daily[
                    "precipitation_probability_max"
                ][index],
                "wind_speed_max_kmh": daily["wind_speed_10m_max"][index],
            }
        )

    return {
        "location": f"{geo['name']}, {geo['country']}",
        "days": days,
        "forecast": forecast,
    }