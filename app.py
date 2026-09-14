import os
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv


# ---------------------------------
# Make src/ available for imports
# ---------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


# ---------------------------------
# Load local environment variables
# ---------------------------------

load_dotenv()


# ---------------------------------
# Import our agent
# ---------------------------------

from ai_agent.agent import agent


# ---------------------------------
# Streamlit configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Tool-Using Agent",
    page_icon="🤖",
)

st.title("🤖 AI Tool-Using Agent")

st.caption(
    "Powered by Groq + LangChain + LangGraph"
)


# ---------------------------------
# Initialize conversation history
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------
# Display previous messages
# ---------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------------
# Chat input
# ---------------------------------

user_input = st.chat_input(
    "Ask me something..."
)


# ---------------------------------
# Process user message
# ---------------------------------

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                result = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": user_input,
                            }
                        ]
                    }
                )

                answer = result["messages"][-1].content

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as exc:

                st.error(
                    f"Something went wrong: {exc}"
                )


# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:

    st.header("About")

    st.write(
        """
        This project demonstrates:

        • LLM-powered agents
        • Tool calling
        • LangChain
        • LangGraph
        • Groq API
        • Streamlit
        """
    )

    st.divider()

    if st.button("Clear conversation"):

        st.session_state.messages = []

        st.rerun()