import streamlit as st
from config import WELCOME_MSG
from funcs import chat_history, create_chat, response_generator

#Page Title
st.title("Welcome to Whimsy!")

#Get History or Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Obtain chat object from Gemini Client
chat = create_chat()

# Welcome Message
with st.chat_message("assistant"):
    st.markdown(WELCOME_MSG)

#Load Chat History
chat_history(st)

# Main Chat Logic
if prompt := st.chat_input("Go Ahead and ask Whimsy Something!"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        reply = response_generator(chat, prompt)
        response = st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

# Add CSS for better chat appearance (optional)
st.markdown(
    """
    <style>
    h1 {
        font-family: "Comic Sans MS", cursive, sans-serif;
        color: #FF69B4;
    }
    h2 {
        font-family: "Brush Script MT", cursive;
        color: #4A0082;
    }
    .highlight {
        background-color: yellow;
        padding: 2px 5px;
        border-radius: 3px;
    }
    blockquote {
        background: #f9f9f9;
        border-left: 10px solid #ccc;
        margin: 1.5em 10px;
        padding: 0.5em 10px;
        quotes: "\\201C""\\201D""\\2018""\\2019";
    }
    blockquote:before {
        color: #ccc;
        content: open-quote;
        font-size: 4em;
        line-height: 0.1em;
        margin-right: 0.25em;
        vertical-align: -0.4em;
    }
    blockquote p {
        display: inline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
