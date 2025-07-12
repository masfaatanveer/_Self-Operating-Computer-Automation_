import streamlit as st
import threading
import os
from streamlit_chat import message
import operate.main as main

# Global variables to manage operation state
operation_thread = None
operation_running = False
chat_history = []  # To store chat messages

def run_operation(model, voice_mode, verbose_mode):
    global operation_running
    operation_running = True
    
    try:
        main.main_entry(model, voice_mode, verbose_mode)
    except Exception as e:
        chat_history.append({"message": str(e), "is_user": False})
    
    operation_running = False

def start_operation(api_key):
    global operation_thread
    if not operation_running:
        os.environ["OPENAI_API_KEY"] = api_key
        model = 'gpt-4-with-ocr'  # Default model, modify as needed
        voice_mode = True  # or False, depending on your use case
        verbose_mode = False  # or True, depending on your use case

        # Start the operation in a new thread
        operation_thread = threading.Thread(target=run_operation, args=(model, voice_mode, verbose_mode))
        operation_thread.start()
        chat_history.append({"message": "Operation started!", "is_user": True})

def shutdown_operation():
    global operation_running
    if operation_running:
        operation_running = False
        chat_history.append({"message": "Operation shutdown initiated.", "is_user": True})
    else:
        chat_history.append({"message": "No operation is currently running.", "is_user": True})

# Streamlit UI
st.title("Softtik: Self Operating Computer")

# API Key input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Sidebar for buttons
if st.sidebar.button("Start"):
    if api_key:
        start_operation(api_key)
    else:
        st.sidebar.warning("Please enter an API key to start the operation.")

if st.sidebar.button("Shutdown"):
    shutdown_operation()

# Display chat messages
for chat in chat_history:
    message(chat["message"], is_user=chat["is_user"])
