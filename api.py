# weather_api.py

"""
Fetches real-time weather data using OpenWeatherMap API.
"""

import requests

API_KEY = "bfda1687711abef59290b247ec21bd9e"  # Replace with your key
BASE_URL = "https://api.openweathermap.org/data/2.5"

def get_current_temp(city):
    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return round(data["main"]["temp"], 1)  # e.g., 29.5°C
    else:
        return None

def get_tomorrow_forecast(city):
    url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Get forecast ~24 hours from now
        for entry in data["list"]:
            if "12:00:00" in entry["dt_txt"]:
                temp = round(entry["main"]["temp"], 1)
                description = entry["weather"][0]["description"]
                return temp, description
        return None, None
    else:
        return None, None
