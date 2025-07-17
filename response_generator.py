"""
response_generator.py
---------------------
This module generates human-readable responses based on predicted intent,
city name, and temperature.

Function:
    - generate_response(intent, city, temp)

Inputs:
    - intent (str): Predicted user intent (e.g., 'current_weather')
    - city (str): City name to include in the response
    - temp (str or int): Temperature value to display in the response

Output:
    - str: Natural language response for the chatbot
"""

def generate_response(intent, city="your city", temp="28"):
    if intent == "current_weather":
        return f"The current temperature in {city} is {temp}°C."

    elif intent == "tomorrow_forecast":
        return f"The weather forecast for tomorrow in {city} is {temp}°C with clear skies."

    elif intent == "greeting":
        return "Hello! I can help you with today's or tomorrow's weather."
    
    elif intent == "thank_you":
        return "You are welcome. Let me know how can I help you!"

    elif intent == "unsupported_forecast":
        return "Sorry, I can only tell you about today’s and tomorrow’s weather for now."

    else:
        return "Sorry, I didn’t understand that. Can you rephrase?"
