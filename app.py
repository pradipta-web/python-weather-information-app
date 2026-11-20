import requests

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "country": location.get("country", "Unknown"),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "wind_speed_10m",
            "weather_code"
        ]
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()["current"]


def get_weather_description(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    return descriptions.get(code, "Unknown weather")


def main():
    print("=" * 40)
    print("       WEATHER INFORMATION APP")
    print("=" * 40)

    city = input("\nEnter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    try:
        location = get_coordinates(city)

        if location is None:
            print("\nCity not found!")
            return

        weather = get_weather(
            location["latitude"],
            location["longitude"]
        )

        print("\n" + "=" * 40)
        print("          WEATHER INFORMATION")
        print("=" * 40)

        print(f"City        : {location['name']}")
        print(f"Country     : {location['country']}")
        print(f"Temperature : {weather['temperature_2m']} °C")
        print(f"Feels Like  : {weather['apparent_temperature']} °C")
        print(f"Condition   : {get_weather_description(weather['weather_code'])}")
        print(f"Humidity    : {weather['relative_humidity_2m']}%")
        print(f"Wind Speed  : {weather['wind_speed_10m']} km/h")
        print(f"Precipitation: {weather['precipitation']} mm")

        print("=" * 40)

    except requests.exceptions.RequestException as error:
        print(f"\nConnection error: {error}")

    except (KeyError, IndexError, ValueError):
        print("\nUnable to retrieve weather information.")


if __name__ == "__main__":
    main()