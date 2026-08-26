def build_rag_answer_prompt(
    question: str,
    retrieved_chunks: list[dict],
) -> str:
    """
    Build a prompt for generating an answer from retrieved
    policy-document context.
    """

    context_parts = []

    for index, chunk in enumerate(retrieved_chunks, start=1):
        source = chunk.get("source_filename", "unknown")
        text = chunk.get("text", "")

        context_parts.append(
            f"""
Context {index}
Source: {source}
Content:
{text}
"""
        )

    context = "\n".join(context_parts)

    return f"""
You are a policy question answering assistant.

Answer the user's question ONLY using the information
provided in the context below.

Do NOT use outside knowledge.

Do NOT guess.

Do NOT make up facts.

If the context does not contain enough information to
answer the question, clearly say that the information is
not available in the provided policy documents.

If you cannot answer from the context:
- set "grounded" to false
- use an empty "sources" list
- set "confidence" appropriately low

If the answer is supported by the context:
- set "grounded" to true
- include the relevant source filename(s)
- provide a confidence value between 0 and 1

USER QUESTION:
{question}

RETRIEVED CONTEXT:
{context}

Return ONLY valid JSON.

Do not use Markdown.
Do not use ```json.
Do not add any explanation before or after the JSON.

The JSON must have exactly this structure:

{{
    "answer": "string",
    "sources": ["filename.pdf"],
    "grounded": true,
    "confidence": 0.0
}}

Important:
Analyze the retrieved context carefully.
Answer ONLY from that context.
If the context is insufficient, do not guess.
"""
