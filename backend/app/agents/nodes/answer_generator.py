from app.agents.state import State


def answer_generator_node(state: State) -> dict:

    if state.get("sql_error"):
        return {
            "final_answer": f"unable to complete the query: {state['sql_error']}"
        }

    query_result = state.get("query_result")

    if not query_result:
        return {
            "final_answer": "the query returned no results"
        }

    return {
        "final_answer":(
            f"Here are the query results:\n{query_result}"
        )
    }

