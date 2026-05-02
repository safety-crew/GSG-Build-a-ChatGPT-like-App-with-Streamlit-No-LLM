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

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate mock responses
def generate_mock_response(user_input):
    """Generate a mock response based on user input without using any LLM."""
    responses = [
        f"That's interesting! You said: '{user_input}'. Tell me more about that.",
        f"I understand you're asking about: '{user_input}'. Here's what I think...",
        f"Great question! Regarding '{user_input}', there are several perspectives to consider.",
        f"Thanks for sharing: '{user_input}'. Let me help you with that.",
        f"You mentioned: '{user_input}'. That's a fascinating topic to explore!",
        f"Interesting point about '{user_input}'. Here's my take on it.",
        f"I see you're interested in '{user_input}'. Let's discuss this further.",
        f"Regarding '{user_input}', there are many ways to approach this.",
    ]

    # Simple keyword-based responses for more context-aware mock replies
    lower_input = user_input.lower()

    if "hello" in lower_input or "hi" in lower_input:
        return "Hello! How can I help you today? Feel free to ask me anything!"
    elif "how are you" in lower_input:
        return "I'm doing great, thanks for asking! I'm a simple chat app running locally on your machine. How can I assist you?"
    elif "bye" in lower_input or "goodbye" in lower_input:
        return "Goodbye! It was nice chatting with you. Feel free to come back anytime!"
    elif "help" in lower_input:
        return "I'm here to help! You can ask me anything, and I'll do my best to respond. Just type your message in the chat input below."
    elif "what can you do" in lower_input:
        return "I can chat with you about various topics! I'm a simple chat application that generates responses locally without using any external AI services. Try asking me anything!"
    elif "python" in lower_input:
        return "Python is a great programming language! It's versatile, easy to learn, and has a huge ecosystem of libraries. Are you working on a Python project?"
    elif "streamlit" in lower_input:
        return "Streamlit is an amazing framework for building data apps and web interfaces with Python! It's what powers this chat application. Would you like to know more about it?"
    elif "code" in lower_input:
        return "I can help discuss code-related topics! Whether it's Python, JavaScript, or any other language, feel free to ask questions or share your thoughts."
    elif "weather" in lower_input:
        return "I don't have access to real-time weather data, but I can chat about weather concepts, climate, or help you think through weather-related questions!"
    elif "joke" in lower_input:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
            "Why did the Python programmer need glasses? Because he couldn't C#! 😂",
            "What's a programmer's favorite hangout place? Foo Bar! 🍺",
            "Why do Java programmers wear glasses? Because they don't C#! 😎",
        ]
        return random.choice(jokes)
    elif "thank" in lower_input:
        return "You're welcome! I'm happy to help. Is there anything else you'd like to chat about?"

    # Default random response
    return random.choice(responses)


