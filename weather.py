import os
import requests
from dotenv import load_dotenv

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────
WEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ── Weather Fetcher ───────────────────────────────────────────────────────────
def get_weather(city: str) -> dict:
    """Fetch weather data from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 404:
        raise ValueError(f"City '{city}' not found.")
    if response.status_code != 200:
        raise ConnectionError(f"API error: {response.status_code}")

    return response.json()

# ── Smart Summary (no AI needed!) ─────────────────────────────────────────────
def get_summary(weather_data: dict) -> str:
    """Generate a friendly summary using simple logic."""
    temp        = weather_data["main"]["temp"]
    humidity    = weather_data["main"]["humidity"]
    wind_speed  = weather_data["wind"]["speed"]
    description = weather_data["weather"][0]["description"]

    # Temperature tip
    if temp >= 35:
        temp_tip = "It's very hot outside. Stay hydrated and avoid direct sunlight."
    elif temp >= 25:
        temp_tip = "It's warm and pleasant. Light clothes are perfect."
    elif temp >= 15:
        temp_tip = "Mild weather today. A light jacket might be handy."
    elif temp >= 5:
        temp_tip = "It's cold outside. Wear a coat and stay warm."
    else:
        temp_tip = "Freezing temperatures! Bundle up with heavy layers."

    # Rain tip
    rain_tip = ""
    if any(word in description for word in ["rain", "drizzle", "shower", "storm"]):
        rain_tip = " Don't forget your umbrella!"

    # Wind tip
    wind_tip = ""
    if wind_speed > 10:
        wind_tip = " It's quite windy, hold on to your hat!"

    return temp_tip + rain_tip + wind_tip

# ── Display ───────────────────────────────────────────────────────────────────
def display_weather(weather_data: dict):
    """Print weather info in the terminal."""
    city        = weather_data["name"]
    country     = weather_data["sys"]["country"]
    temp        = weather_data["main"]["temp"]
    feels_like  = weather_data["main"]["feels_like"]
    humidity    = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"].capitalize()
    wind_speed  = weather_data["wind"]["speed"]
    summary     = get_summary(weather_data)

    print("\n" + "═" * 50)
    print(f"  🌍  Weather in {city}, {country}")
    print("═" * 50)
    print(f"  🌡️  Temperature : {temp}°C  (feels like {feels_like}°C)")
    print(f"  🌤️  Condition   : {description}")
    print(f"  💧  Humidity    : {humidity}%")
    print(f"  💨  Wind Speed  : {wind_speed} m/s")
    print("─" * 50)
    print(f"  💡  Tip: {summary}")
    print("═" * 50 + "\n")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("\n🌦️  Weather App — Powered by OpenWeatherMap")
    print("Type a city name to get the weather. Type 'quit' to exit.\n")

    while True:
        city = input("Enter city name: ").strip()

        if city.lower() in ("quit", "exit", "q"):
            print("Goodbye! 👋")
            break

        if not city:
            print("Please enter a city name.\n")
            continue

        try:
            print("⏳ Fetching weather data...")
            weather_data = get_weather(city)
            display_weather(weather_data)

        except ValueError as e:
            print(f"❌ {e}\n")
        except ConnectionError as e:
            print(f"❌ {e}\n")
        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")

if __name__ == "__main__":
    main()