import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

st.set_page_config(page_title="AI Multiverse", page_icon="🌌")

st.title("🌌 AI Multiverse")
st.write("Talk with different AI personalities from across the multiverse.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

personality = st.sidebar.selectbox(
    "🎭 Choose a Personality",
    [
        "An Expert Hacker",
        "A HR",
        "A Crazy Tech Fresher"
    ]
)

st.sidebar.header("⚙️ Multiverse Controls")

intensity = st.sidebar.slider(
    "Character Intensity",
    min_value=1,
    max_value=20,
    value=5,
    help="Higher intensity makes the AI stay more deeply in character."
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

user_message = st.text_input("💬 Say something...")

if st.button("🚀 SEND"):

    if user_message:

        ai_instructions = f"""
You are acting as {personality}.

Stay completely in character.

Character intensity level: {intensity}/20.

Respond naturally to the following message:

{user_message}
"""

        with st.spinner("🌌 Connecting to the Multiverse..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_instructions
            )

        st.success("Response received!")

        st.session_state.chat_history.append(
            {
                "role": "You",
                "message": user_message
            }
        )

        st.session_state.chat_history.append(
            {
                "role": personality,
                "message": response.text
            }
        )

    else:
        st.warning("⚠️ Please enter a message first.")

st.divider()
st.subheader("💬 Chat History")

if len(st.session_state.chat_history) == 0:
    st.info("No conversation yet.")

for chat in st.session_state.chat_history:

    if chat["role"] == "You":
        with st.chat_message("user"):
            st.write(chat["message"])

    else:
        with st.chat_message("assistant"):
            st.markdown(f"**{chat['role']}**")
            st.write(chat["message"])
