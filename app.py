import streamlit as st
st.title("AI Multiverse ")

personality=st.sidebar.selectbox("Who do you want to talk to?",[
    "An Expert Hacker", "A HR", "A crazy Tech fresher"
])
st.sidebar.header("🌌 Multiverse Controls")

intensity = st.sidebar.slider(
    "Character Intensity",
    1, 20, 5,
    help="Higher intensity makes the AI stay more deeply in character."
)

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_message=st.text_input("Say something:")
if st.button("SEND"):
    if user_message:
        ai_instructions= f"You are acting as {personality}.Respond to the message sent by the user staying completely in character: {user_message} "
        with st.spinner("Connecting to the multiverse!........"):
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )

            st.success("Message received")
            st.write(response.text)


    else:
        st.warning("please enter message first")


