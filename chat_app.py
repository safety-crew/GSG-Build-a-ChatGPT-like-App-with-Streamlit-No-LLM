import streamlit as st
import random
import time

# Set page title and configuration
st.set_page_config(
    page_title="ChatGPT Clone - No LLM",
    page_icon="💬",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Page title and description
st.title("💬 ChatGPT Clone - No LLM Required")
st.markdown("""
This is a simple chat application built with Streamlit that simulates ChatGPT-like responses
without using any external LLM or API. All responses are generated locally using Python!
""")