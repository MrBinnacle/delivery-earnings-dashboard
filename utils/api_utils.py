import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_weather(location="Maywood"):
    """Fetch weather data for a given location."""
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": os.getenv("OPENWEATHER_API_KEY")}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error fetching weather: {response.status_code}")

def fetch_events(location="Maywood"):
    """Fetch local events from Ticketmaster API."""
    url = f"https://app.ticketmaster.com/discovery/v2/events.json"
    params = {"apikey": os.getenv("TICKETMASTER_CONSUMER_KEY"), "city": location}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error fetching events: {response.status_code}")
