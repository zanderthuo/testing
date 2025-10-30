import streamlit as st
import requests
import os

st.set_page_config(page_title="DT1-25 Chat", page_icon="💬")
st.title("A Simple Chat System 💬")

API_URL = os.getenv("API_URL", "http://localhost:5001")
st.caption(f"Connected to backend: {API_URL}")

user_input = st.text_input("Ask me something:")

if st.button("Chat"):
    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Contacting backend..."):
            try:
                res = requests.post(f"{API_URL}/chat", json={"input": user_input}, timeout=60)
                if res.status_code == 200:
                    data = res.json()
                    st.success("Response received ✅")
                    st.write(data.get("answer", "No response content"))
                else:
                    st.error(f"Request failed: {res.status_code}")
                    st.text(res.text)
            except Exception as e:
                st.error(f"Error: {e}")
