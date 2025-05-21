import streamlit as st
import requests

st.set_page_config(page_title="SmartMedicalBot", layout="centered")
st.title("SmartMedicalBot")
st.markdown("Enter your symptoms and the bot will respond with preliminary medical advice.")

user_input = st.text_input("Enter your symptoms here:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a symptom.")
    else:
        url = "https://udify.app/chat/BXE7UHClh3Liaf7T"
        headers = {
            "Authorization": "MvMNfrvLnaD8mR9eKbP1Q4I1",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": user_input,
            "response_mode": "blocking"
        }

        with st.spinner("Please wait..."):
            response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            reply = result.get("answer") or result.get("response") or "No response received."
            st.success("Agent Answer:")
            st.write(reply)
        else:
            st.error(f"An error occurred while communicating with the bot. Status symbol: {response.status_code}")
            st.write(response.text)
