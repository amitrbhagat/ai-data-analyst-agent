from app.agents.state import State
from app.llm.provider import provide_response
import json


def synthesis_node(state: State) -> dict:
    question = state["question"]
    query_result = state.get("query_result")
    rag_answer = state.get("rag_answer")

    prompt = f"""
You are an AI Data Analyst assistant.

The user asked:
{question}

Database result:
{query_result}

Policy/document answer:
{rag_answer}

Your task is to combine the database result and document/policy information
into one accurate answer.

Rules:
1. Use only the provided database result and document answer.
2. Do not invent facts.
3. Clearly distinguish numerical/business data from policy information.
4. If one source does not contain useful information, use the other source.
5. Answer the user's question directly.
6. Keep the answer concise but useful.

Return ONLY valid JSON in this format:

{{
    "answer": "final combined answer",
    "confidence": 0.0
}}
"""

    response = provide_response(prompt, temperature=0.1)

    try:
        result = json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError("Synthesis LLM returned invalid JSON.") from e

    return {
        "synthesis_answer": result["answer"]
    }