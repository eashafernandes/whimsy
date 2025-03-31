from config import GEMINI, BOT_PROMPT_STYLE
from google import genai

def chat_history(st):
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def create_chat():
    client = genai.Client(api_key=GEMINI)
    chat = client.chats.create(model='gemini-2.0-flash', history=[])
    chat.send_message(BOT_PROMPT_STYLE)
    return chat

def response_generator(chat, prompt):
    response = chat.send_message(prompt)
    return response.text