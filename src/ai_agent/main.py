from .agent import agent


while True:
    user_input = input("\nYou: ")

    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

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

        print("\nAI:", result["messages"][-1].content)

    except Exception as exc:
        print("\nSomething went wrong.")

        error_message = str(exc)

        if "credit_balance_exhausted" in error_message:
            print(
                "OpenAI API credits are exhausted. "
                "Please add API credits and try again."
            )
        else:
            print(f"Error: {error_message}")