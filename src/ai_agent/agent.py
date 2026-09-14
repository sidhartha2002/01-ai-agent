from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from .tools import calculator


load_dotenv()


model = ChatGroq(
    model="openai/gpt-oss-20b",
)


agent = create_agent(
    model=model,
    tools=[calculator],
    system_prompt=(
        "You are a helpful AI assistant. "
        "Use the calculator tool whenever accurate arithmetic is required."
    ),
)