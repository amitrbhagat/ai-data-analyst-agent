from app.agents.state import State


def answer_generator_node(state: State) -> dict:
    print("[NODE] answer_generator")

    intent = state["intent"].upper()


    if intent=="SQL":

        if state["query_result"] is not None:
            answer = f"Here are the query results:\n{state['query_result']}"
        else:
            answer = (
                f"Unable to retrieve the requested data .."
                f"{state.get('sql_error', '')}"
            )    

        return {
            "final_answer": answer
        }    


    if intent == "RAG":

        return {
            "final_answer": state.get(
                "rag_answer",
                "I could not find an answer uin available documents ."
            )
        }


    if intent == "HYBRID":

        return {
            "final_answer": state.get(
                "synthesis_answer",
                "Unable to combine the requested data and policy information."
            )
        }

    raise ValueError(f"Unsupported intent: {intent}")
