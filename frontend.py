import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")


system_prompt = st.text_area("Define Your AI Agent:", height=70, placeholder="Type Your System Prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
else:
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything!")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(f"Error: {response_data['error']}")
                else:
                    st.subheader("Agent Response")
                    st.markdown(f"**Final Response:** {response_data}")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        
        except requests.exceptions.RequestException as e:
            st.error(f"Connection Error: Unable to reach API.\n\nDetails: {e}")
    else:
        st.warning("Please enter a query before submitting!")
