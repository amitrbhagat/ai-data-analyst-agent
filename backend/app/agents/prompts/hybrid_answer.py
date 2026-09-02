def build_hybrid_answer_prompt(
    question: str,
    sql_result: str,
    rag_answer: str,
    rag_sources: list[str],
) -> str:

    sources_text = "\n".join(
        f"- {source}"
        for source in rag_sources
    )

    return f"""
You are an AI Data Analyst assistant.

Your task is to combine two independently produced answers:
1. A database result
2. A grounded document/policy answer

Create one coherent answer to the user's original question.

Original question:
{question}

DATABASE RESULT:
{sql_result}

DOCUMENT / POLICY ANSWER:
{rag_answer}

DOCUMENT SOURCES:
{sources_text}

Instructions:

1. Directly answer the original question.
2. Combine the database result and document answer into ONE coherent narrative.
3. Do not simply place the SQL answer and policy answer into two separate paragraphs.
4. Reference specific data points from the database result when relevant.
5. Reference specific policy details when relevant.
6. Only make connections between the data and policy that are explicitly supported by the provided information.
7. Never invent facts, policy rules, relationships, calculations, or conclusions.
8. If the database result does not support a claim, do not make that claim.
9. If the document answer does not support a policy claim, do not make that claim.
10. Preserve the groundedness of the document answer.
11. If one source is not relevant to part of the question, do not force it into the answer.
12. Keep the final response concise and useful.

Return ONLY valid JSON.

Required format:

{{
    "answer": "The final combined answer.",
    "sources": {sources_text!r},
    "data_used": true
}}
"""
