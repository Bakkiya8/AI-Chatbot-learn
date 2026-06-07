import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# ── Client ────────────────────────────────────────────────────────────────────
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Groq Chatbot")
st.caption("Powered by llama-3.3-70b-versatile")

# ── Memory (same list you had, but stored in session_state) ───────────────────
# Your original code:  messages = []
# Streamlit reruns the script on every interaction, so we use session_state
# to keep the list alive between reruns — that's the only real difference.
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Render chat history ───────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── Chat input (replaces input() from terminal) ───────────────────────────────
user_input = st.chat_input("You:")

if user_input:

    # Same as your: messages.append({"role": "user", ...})
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Same as your: client.chat.completions.create(...)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages,
            )
            reply = response.choices[0].message.content

        st.write(reply)

    # Same as your: messages.append({"role": "assistant", ...})
    st.session_state.messages.append({"role": "assistant", "content": reply})