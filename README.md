# 🤖 AI Tool-Using Agent

### An AI agent that doesn't just answer — it knows when to use a tool.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-1C3C3C)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-1C3C3C)](https://www.langchain.com/langgraph)
[![Groq](https://img.shields.io/badge/Groq-LLM-F55036)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

> A practical AI agent built with Python, LangChain, LangGraph and Groq that can reason about a user's request, decide when a tool is needed, execute the tool, and use the result to produce a final response.

---

## 🚀 Live Demo

### 👉 [Try the AI Agent](https://ai-tool-agent-01.streamlit.app/)

Open the live application and ask it something like:

> **What is 45 × 27?**

The agent can recognize that accurate arithmetic is better handled by a dedicated Python tool rather than relying only on the language model.

---

### 👀 What does it do?

This project demonstrates the difference between a **normal LLM chatbot** and a **tool-using AI agent**.

A traditional chatbot might do:

```
User
  ↓
LLM
  ↓
Answer

This project can do:

User
  ↓
AI Agent
  ↓
Does this request require a tool?
       │
       ├── No ────────────────► LLM → Answer
       │
       └── Yes
             ↓
        Calculator Tool
             ↓
          Tool Result
             ↓
             LLM
             ↓
          Final Answer

```

### Agent reasoning flow :

```
1. Understand the request
2. Determine that arithmetic is required
3. Invoke the calculator tool
4. Receive the result: 1215
5. Generate the final response
```

### Features :

```
| Feature                 | Description                                       |
| ----------------------- | ------------------------------------------------- |
| 💬 Conversational UI    | Chat with the agent through a Streamlit interface |
| 🧠 Agent reasoning      | Determines whether a tool is required             |
| 🔧 Tool calling         | Dynamically invokes Python tools                  |
| 🧮 Calculator           | Performs arithmetic using a dedicated Python tool |
| ⚡ Fast inference        | Powered by Groq                                   |
| 🕸️ Agent orchestration | Built with LangChain + LangGraph                  |
| ☁️ Cloud deployment     | Deployed using Streamlit Community Cloud          |
| 🔐 Secret management    | API keys kept outside source control              |

```
### Checkout its working --
<img width="1366" height="3825" alt="image" src="https://github.com/user-attachments/assets/edbb5f3e-077f-4e3d-8736-1d0738791e5b" />
