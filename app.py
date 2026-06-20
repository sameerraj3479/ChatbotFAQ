import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Smart FAQ Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Smart FAQ Assistant")


st.sidebar.title("About")
st.sidebar.info("""
Topics Covered:

• AI & Machine Learning
• Python Programming
• Computer Science Basics
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

question = st.text_input(
    "Ask your question",
    placeholder="Example: What is AI?"
)

if st.button("Send") and question:

    answer = get_response(question)

    st.session_state.messages.append(
        {
            "user": question,
            "bot": answer
        }
    )

for msg in reversed(st.session_state.messages):

    st.info(f"👤 You: {msg['user']}")
    st.success(f"🤖 Bot: {msg['bot']}")

st.markdown("---")
st.caption("Built with Python, Streamlit and Scikit-Learn")

