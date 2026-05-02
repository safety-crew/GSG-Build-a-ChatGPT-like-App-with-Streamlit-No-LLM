# ChatGPT Clone - No LLM Required 💬

Gaza Sky Geeks Technical Task for Agentic AI & Retrieval-Augmented Generation (RAG) Bootcamp – Nablus

A simple ChatGPT-style chat application built with Streamlit that generates mock responses locally without using any external Large Language Model (LLM) or API.

## Features ✨

- 💬 **ChatGPT-style Interface**: Clean, modern chat interface using Streamlit's chat components
- 🚀 **Built with Streamlit**: Fast, responsive web app using Python
- 🤖 **No External LLM**: All responses generated locally using simple Python logic
- 💾 **Chat History**: Conversation history preserved in session state
- ⚡ **Fast Responses**: Instant local responses without API calls
- 🎯 **Keyword-Based Responses**: Context-aware mock responses based on keywords
- 📊 **Chat Statistics**: Track message count in the sidebar
- 🗑️ **Clear History**: Option to clear chat history

## How It Works 🛠️

This application demonstrates:
1. **Streamlit Chat Components**: Using `st.chat_message` and `st.chat_input`
2. **Session State Management**: Storing conversation history in `st.session_state.messages`
3. **Local Response Generation**: Simple Python function that generates mock responses
4. **Typing Effect**: Simulated typing animation for better UX
5. **Keyword Matching**: Context-aware responses based on user input

## Installation 📦

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/GSG-Build-a-ChatGPT-like-App-with-Streamlit-No-LLM.git
   cd GSG-Build-a-ChatGPT-like-App-with-Streamlit-No-LLM
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

Run the application:
```bash
streamlit run chat_app.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use 💡

1. Type your message in the chat input at the bottom
2. Press Enter or click the send button
3. The app will generate a mock response locally
4. Continue the conversation - your chat history is preserved!

## Example Interactions 📝

Try these messages to see different responses:
- "Hello!" or "Hi there!"
- "How are you?"
- "Tell me a joke"
- "What can you do?"
- "Help me with Python"
- "Tell me about Streamlit"
- "Thank you for your help"

## Code Structure 📁

```
.
├── chat_app.py          # Main application file
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Key Components Explained 🔧

### 1. Session State Initialization
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

### 2. Display Chat History
```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

### 3. Chat Input
```python
if prompt := st.chat_input("Type your message here..."):
    # Process user input and generate response
```

### 4. Mock Response Generation
```python
def generate_mock_response(user_input):
    # Generate context-aware responses based on keywords
    # Returns appropriate mock response
```

## Tech Stack 🛠️

- **Python**: Core programming language
- **Streamlit**: Web framework for building the chat interface
- **No External APIs**: All logic runs locally

## Learning Outcomes 🎓

This project demonstrates:
- Streamlit basics and chat components
- Session state management in Streamlit
- Building interactive web apps with Python
- Simple state management and data persistence
- Creating responsive UI without external dependencies

## Video Demo 🎥

Check out the [2-minute YouTube video](https://youtube.com/your-video-link) demonstrating:
- How the app runs
- User interaction walkthrough
- Code explanation
- How responses are simulated locally

## Contributing 🤝

Feel free to fork this project and make it your own! Some ideas:
- Add more sophisticated response logic
- Implement different response strategies
- Add user customization options
- Create different response personalities

## License 📄

This project is open source and available for educational purposes.

## Author 👨‍💻

Built with ❤️ using Streamlit

---

**Note**: This is a demonstration project that simulates chat responses. For production applications with real AI capabilities, consider integrating with actual LLM APIs.
