import streamlit as st
from openai import OpenAI

# Define your OpenAI API key
OPENAI_API_KEY = "OpenAI API key"  # Replace with your API key

# Instantiate the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to query OpenAI API
def query_openai_api(prompt, history):
    try:
        messages = [{"role": "system", "content": "You are a helpful assistant for solving Python coding problems."}]
        messages += history
        messages.append({"role": "user", "content": prompt})

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use gpt-3.5-turbo or gpt-4
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to OpenAI API: {e}"

# Streamlit Chatbot App
def main():
    # Streamlit page configuration
    st.set_page_config(page_title="Python LeetCode Helper", layout="wide")

    # Title and Introduction
    st.title("💬 Python LeetCode Helper Chatbot")
    st.markdown("### Solve your Python coding problems interactively!")

    # Initialize session state for conversation history
    if "history" not in st.session_state:
        st.session_state["history"] = []

    # Chat Interface
    chat_container = st.container()

    with chat_container:
        # Display conversation history
        if st.session_state["history"]:
            for i, (user_msg, bot_msg) in enumerate(st.session_state["history"]):
                st.markdown(f"**You:** {user_msg}")
                st.markdown(f"**Helper:** {bot_msg}")

        # User Input
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_area("Your Question:", placeholder="Ask a Python-related coding question...")
            submit_button = st.form_submit_button("Send")

        # Process User Input
        if submit_button and user_input.strip():
            # Append user message to conversation history
            st.session_state["history"].append((user_input, "Thinking..."))

    # Process AI Response
    if st.session_state["history"] and st.session_state["history"][-1][1] == "Thinking...":
        user_msg = st.session_state["history"][-1][0]
        bot_response = query_openai_api(user_msg, [{"role": "user", "content": msg[0]} for msg in st.session_state["history"][:-1]])
        st.session_state["history"][-1] = (user_msg, bot_response)

    # Clear Chat Button
    if st.button("Clear Chat"):
        st.session_state["history"] = []

# Run the app
if __name__ == "__main__":
    main()
