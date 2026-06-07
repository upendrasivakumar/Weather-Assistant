# 🌤️ AI Weather Assistant

An AI-powered Weather Assistant built using **FastAPI**, **Streamlit**, **Groq LLM**, and the **OpenWeatherMap API**.

The application fetches real-time weather data for a given city and uses a Large Language Model (LLM) to generate natural-language responses based only on the retrieved weather information.

---

## 🚀 Features

* Get real-time weather information for any city
* AI-generated weather responses using Groq LLM
* Clean and simple Streamlit user interface
* FastAPI backend for API handling
* OpenWeatherMap API integration
* Secure API key management using `.env`

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI Model

* Groq
* Llama 3.3 70B Versatile

### Weather API

* OpenWeatherMap API

---

## 📂 Project Structure

```text
AI_Weather_Assistant/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI_Weather_Assistant
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweathermap_api_key
```

---

## ▶️ Run the Backend

Navigate to the backend folder and start FastAPI:

```bash
uvicorn main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

---

## ▶️ Run the Frontend

Navigate to the frontend folder and run:

```bash
streamlit run app.py
```

Frontend will run at:

```text
http://localhost:8501
```

---

## 📌 How It Works

1. User enters a city name and weather-related question.
2. Streamlit sends the request to the FastAPI backend.
3. FastAPI fetches live weather data from OpenWeatherMap.
4. Weather details are passed to the Groq LLM.
5. The LLM generates a concise weather response using only the provided weather data.
6. The response is displayed in the Streamlit interface.

---

## Example

### Input

```text
City: Hyderabad
Question: What is the weather today?
```

### Output

```text
The temperature in Hyderabad is 34°C with 60% humidity and a wind speed of 4.2 m/s.
```

---

## Future Improvements

* 5-day weather forecast
* Weather charts and visualizations
* Voice-based weather queries
* Location auto-detection
* Multi-language support

---

## 👨‍💻 Author

Siva Madala

B.Tech Graduate | Python Developer | Generative AI Enthusiast

LinkedIn: https://www.linkedin.com/in/madalaupendrasivakumar

GitHub: https://github.com/upendrasivakumar
