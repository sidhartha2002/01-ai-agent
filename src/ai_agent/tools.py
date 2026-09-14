from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Calculate a basic arithmetic expression.
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {},
        )

        return str(result)

    except Exception as exc:
        return f"Calculation error: {exc}"