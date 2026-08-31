import json

from pydantic import ValidationError

from app.rag.retrieval import retrieve_relevant_chunks
from app.agents.prompts.rag_answer import build_rag_answer_prompt
from app.llm.provider import provide_response
from app.schemas.rag import RAGAnswerResult


# Tune this based on the distance values you observed
# during your retrieval testing.
DEFAULT_DISTANCE_THRESHOLD = 0.7


def _clean_llm_response(response: str) -> str:
    """
    Remove Markdown code fences if the LLM returns them
    even though the prompt asks for plain JSON.
    """

    response = response.strip()

    if response.startswith("```json"):
        response = response[len("```json"):].strip()

    elif response.startswith("```"):
        response = response[len("```"):].strip()

    if response.endswith("```"):
        response = response[:-3].strip()

    return response


def _parse_rag_response(response: str) -> RAGAnswerResult:
    """
    Parse the LLM response and validate it using Pydantic.
    """

    cleaned_response = _clean_llm_response(response)

    try:
        parsed_response = json.loads(cleaned_response)

    except json.JSONDecodeError as e:
        raise ValueError(
            "LLM returned invalid JSON for RAG answer."
        ) from e

    try:
        result = RAGAnswerResult(**parsed_response)

    except ValidationError as e:
        raise ValueError(
            "LLM RAG response failed Pydantic validation."
        ) from e

    return result


def answer_from_documents(
    question: str,
    distance_threshold: float = DEFAULT_DISTANCE_THRESHOLD,
) -> RAGAnswerResult:
    """
    Answer a user question using the available policy documents.

    Retrieval is filtered using a distance threshold.
    If no relevant chunks are found, the LLM is not called.
    """

    # ---------------------------------------------------------
    # Layer 1: Retrieve relevant chunks
    # ---------------------------------------------------------

    retrieved_chunks = retrieve_relevant_chunks(
        query=question,
        top_k=3,
        distance_threshold=distance_threshold,
    )

    # ---------------------------------------------------------
    # Layer 1: Deterministic "I don't know"
    # ---------------------------------------------------------

    if not retrieved_chunks:
        return RAGAnswerResult(
            answer=(
                "I don't have enough information in the "
                "available policy documents to answer this question."
            ),
            sources=[],
            grounded=False,
            confidence=0.0,
        )

    # ---------------------------------------------------------
    # Layer 2: Ask the LLM using ONLY retrieved context
    # ---------------------------------------------------------

    prompt = build_rag_answer_prompt(
        question=question,
        retrieved_chunks=retrieved_chunks,
    )

    response = provide_response(
        prompt,
        temperature=0.1,
    )

    # ---------------------------------------------------------
    # Parse + validate LLM response
    # ---------------------------------------------------------

    result = _parse_rag_response(response)

    return result
