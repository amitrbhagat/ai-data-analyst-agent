import json

from app.agents.state import State
from app.agents.prompts.hybrid_answer import build_hybrid_answer_prompt
from app.llm.provider import provide_response


def synthesis_node(state: State) -> dict:
    question = state["question"]
    query_result = state["query_result"]
    rag_answer = state["rag_answer"]
    retrieved_documents = state["retrieved_documents"]

    # Convert SQL result into readable text for the LLM
    if query_result:
        sql_result_text = json.dumps(
            query_result,
            indent=2,
            default=str
        )
    else:
        sql_result_text = "No database result available."

    # Ensure sources are always a list
    rag_sources = retrieved_documents or []

    prompt = build_hybrid_answer_prompt(
        question=question,
        sql_result=sql_result_text,
        rag_answer=rag_answer or "No document answer available.",
        rag_sources=rag_sources,
    )

    response = provide_response(
        prompt,
        temperature=0.1
    )

    # Parse structured LLM response
    try:
        parsed_response = json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError(
            "LLM returned invalid JSON during hybrid synthesis."
        ) from e

    # Basic validation
    if "answer" not in parsed_response:
        raise ValueError(
            "Hybrid synthesis response is missing 'answer'."
        )

    return {
        "hybrid_answer": parsed_response["answer"]
    }
