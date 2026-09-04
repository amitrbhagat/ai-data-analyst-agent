from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.graph import graph



router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/api/chat")
def chat(request: ChatRequest):

    initial_state = {
        "question": request.question,
        "conversation_history": [],
        "intent": "",
        "database_schema": "",
        "generated_sql": None,
        "sql_validation_result": None,
        "sql_error": None,
        "query_result": None,
        "retrieved_documents": None,
        "rag_answer": None,
        "hybrid_answer": None,
        "data_summary": None,
        "analysis": None,
        "chart_type": None,
        "chart_config": None,
        "final_answer": None,
        "retry_count": 0,
    }


    try:
        result = graph.invoke(initial_state)

        return {
            "final_answer": result.get("final_answer"),
            "generated_sql": result.get("generated_sql"),
            "query_result": result.get("query_result"),
            "chart_type": result.get("chart_type"),
            "chart_config": result.get("chart_config"),
            "sources": result.get("retrieved_documents") or [],
        }

    except Exception as e:
        return {
            "error": str(e)
        }
        