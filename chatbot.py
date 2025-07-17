"""
chatbot.py
----------
Main script for the WeatherBot terminal chatbot.

This script:
- Takes user queries via terminal input.
- Uses an ML model to detect user intent.
- Identifies city names from queries.
- Generates an appropriate weather-related or general response.

Input: User query via terminal
Output: Printed chatbot response
"""


from model import detect_intent
from response_generator import generate_response

# List of cities the chatbot can recognize in queries
CITIES = [
    "delhi", "mumbai", "bangalore", "chennai", "hyderabad",
    "pune", "kolkata", "gurgaon", "manali", "shimla"
]

def extract_city(query):
    """
    Extract the city name from the user query if present.

    Parameters:
        query (str): The user input text

    Returns:
        str: Capitalized city name if found, else "your city"
    """
    query = query.lower()
    for city in CITIES:
        if city in query:
            return city.capitalize()
    return "your city"

print("Welcome to the WeatherBot!")
print("Type your weather question (or type 'exit' to quit):")

while True:
    query = input("\nYou: ")
    if query.lower() == "exit":
        print("WeatherBot: Goodbye! Stay safe.")
        break
    intent = detect_intent(query) # Get predicted intent using model
    city = extract_city(query)
    response = generate_response(intent, city=city, temp="30")
    print(f"WeatherBot: {response}")
