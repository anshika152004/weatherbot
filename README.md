# Chat-based Weather Assistant (Mini AI Project)

## Overview
This is a rule-based chatbot that answers simple weather-related questions. It detects user intent and returns template-based responses.

## Features
- Detects intent: current weather, tomorrow's forecast, greetings
- Responds based on rule-based classification
- No external API or real-time weather data needed

## How to Run
1. Clone or download the files
2. Run `chatbot.py` using Python 3

```bash
python chatbot.py

## Real Weather API
Currently, the chatbot uses static temperature data for demonstration. In future versions, it can be integrated with a real-time weather API like WeatherAPI to fetch live weather data based on user-input cities. This would allow dynamic responses based on actual current and forecasted weather conditions.