import streamlit as st
import requests

st.set_page_config(page_title="Weather Assistant", page_icon="🌤️")

S_URL = st.secrets["BACKEND_URL"]

st.title("🌤️ Weather Assistant")

city = st.text_input("City", placeholder="Enter city name")
question = st.text_input(
    "Question",
    placeholder="What is the weather today?"
)

if st.button("Get Weather"):

    if not city or not question:
        st.warning("Please enter both city and question.")
    else:
        try:
            with st.spinner("Getting weather information..."):

                res = requests.post(
                    f"{S_URL}/get_weather",
                    params={
                        "city": city,
                        "question": question
                    }
                )

            if res.status_code == 200:

                answer = res.json()["answer"]

                st.markdown("### 🌦️ Weather Report")
                st.container(border=True).write(answer)

            else:
                st.error("Failed to get response from server.")

        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running.")
