import json
from app.agents.state import State
from app.agents.prompts.hybrid_answer import build_hybrid_answer_prompt
from app.llm.provider import provide_response



def synthesis_node(state: State) -> dict:
    question = state["question"]

    query_result = state.get("query_result")
    rag_answer = state.get("rag_answer")
    rag_sources = state.get("retrieved_documents") or []

    sql_result = str(query_result)

    prompt = build_hybrid_answer_prompt(
        question=question,
        sql_result=sql_result,
        rag_answer=rag_answer or "",
        rag_sources=rag_sources,
    )

    response = provide_response(
        prompt,
        temperature=0.1,
    )

    try:
        result = json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError(
            "Hybrid synthesis returned invalid JSON."
        ) from e

    return {
        "synthesis_answer": result["answer"]
    }
