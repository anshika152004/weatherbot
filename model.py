
"""
model.py
--------
This module trains and uses a text classification model to detect the user's intent
based on their weather-related query.

- Trains a Logistic Regression model on TF-IDF features.
- Saves and loads the model and vectorizer using joblib.

Input: A user query (string)
Output: Predicted intent (string)
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

"""
    Trains a logistic regression model on labeled query-intent data from 'mock_data.csv'.
    Saves the trained model and vectorizer to disk.

    Expects:
        - 'mock_data.csv' to contain two columns: 'user_query' and 'intent'
    """

def train_model():
    data = pd.read_csv("mock_data.csv", comment="#")  # Read training data  
    X = data['user_query']
    y = data['intent']

    vectorizer = TfidfVectorizer()  # Convert text to numerical features using TF-IDF
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()  # Train the intent classification model
    model.fit(X_vec, y)

    # Save model and vectorizer
    joblib.dump(model, "intent_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

# Call train only if model doesn't exist
if not os.path.exists("intent_model.pkl"):
    train_model()

# Load the model
model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def detect_intent(query):    # Predicts the intent of a user's query.
    query_vec = vectorizer.transform([query])
    prediction = model.predict(query_vec)
    return prediction[0]
