"""
streamlit_app.py

WeatherBot with Streamlit UI and OpenWeatherMap API to fetch real-time weather for any city mentioned in the query.
"""

import streamlit as st
from model import detect_intent
import requests
from response_generator import generate_response
import re

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        font-size: 18px;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }

    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
    }

    .stChatMessage {
        background-color: #e0f7fa;
        border-radius: 10px;
        padding: 12px;
        margin: 6px 0;
    }
    </style>
""", unsafe_allow_html=True)

API_KEY = "bfda1687711abef59290b247ec21bd9e"  # 🔑 Replace with your actual API key


def extract_city(query):
    """
    Naively extracts a city name using regex based on 'in <city>' or 'at <city>' patterns.

    Args:
        query (str): User's input string.

    Returns:
        str: City name (if found), else default 'your city'.
    """
    match = re.search(r"(in|at)\s+([a-zA-Z\s]+)", query.lower())
    if match:
        return match.group(2).strip()
    return "your city"


def get_weather(city, forecast=False):
    """
    Fetches current or forecasted weather from OpenWeatherMap API.

    Args:
        city (str): City name.
        forecast (bool): Whether to get tomorrow's forecast.

    Returns:
        str: Temperature in Celsius as string or default fallback.
    """
    try:
        if forecast:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url).json()
            temp = res["list"][8]["main"]["temp"]  # ~24 hours later
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url).json()
            temp = res["main"]["temp"]
        return f"{round(temp)}"
    except:
        return "28"  # fallback temperature


# ---------------- Streamlit UI ---------------- #

st.title("🌤️ WeatherBot")
st.write("Ask me anything about today's or tomorrow’s weather in any city!")

user_query = st.text_input("You:", placeholder="e.g. Is it raining in Paris today?")

if user_query:
    intent = detect_intent(user_query)
    city = extract_city(user_query)

    is_forecast = intent == "tomorrow_forecast"
    temp = get_weather(city, forecast=is_forecast)

    response = generate_response(intent, city=city.capitalize(), temp=temp)
    st.write(f"🤖 WeatherBot: {response}")
