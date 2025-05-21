import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Smart Medical Bot", layout="centered")

# Title and description
st.title("🤖 Smart Medical Bot")
st.markdown("Enter the symptoms you're experiencing and the bot will give you a preliminary medical suggestion.")

# User input
user_input = st.text_input("✍️ Enter your symptoms here:")

# Submit button
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter some symptoms.")
    else:
        # API request setup
        url = "https://udify.app/chat/BXE7UHClh3Liaf7T"
        headers = {
            "Authorization": "Bearer app-MvMNfrvLnaD8mR9eKbP1Q4I1",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": user_input,
            "response_mode": "blocking"
        }

        # Send request and show loading spinner
        with st.spinner("Please wait..."):
            response = requests.post(url, json=payload, headers=headers)

        # Handle response
        if response.status_code == 200:
            result = response.json()
            reply = result.get("answer") or result.get("response") or "No reply received."
            st.success("Bot's response:")
            st.write(reply)
        else:
            st.error(f"An error occurred. Status code: {response.status_code}")
            st.write(response.text)
