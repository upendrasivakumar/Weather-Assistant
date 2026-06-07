from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import requests
import os

load_dotenv()

app = FastAPI()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@app.get("/")
def home():
    return {"message": "API Running"}


@app.post("/get_weather")
def get_weather(city: str, question: str):

    weather_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    weather_response = requests.get(weather_url).json()

    temp = weather_response["main"]["temp"]
    humidity = weather_response["main"]["humidity"]
    wind_speed = weather_response["wind"]["speed"]

    prompt = f"""
You are a weather assistant.

Weather Information:
- City: {city}
- Temperature: {temp}°C
- Humidity: {humidity}%
- Wind Speed: {wind_speed} m/s

User Question:
{question}

Answer only using the weather information provided above.
Keep the response short, clear, and natural.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }