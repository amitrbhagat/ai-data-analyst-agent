from app.agents.state import State
from app.services.rag_service import answer_from_documents


def rag_retriever_node(state: State) -> dict:

    question = state["question"]

    result = answer_from_documents(question)

    return {
        "retrieved_documents": result.sources,
        "rag_answer": result.answer,
    }
