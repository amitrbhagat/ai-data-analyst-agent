from app.llm.ollama import generate_embedding


def get_embedding(text: str) -> list[float]:
    """
    Generate an embedding for a single piece of text.
    """

    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    return generate_embedding(text)



def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple text chunks.
    """

    if not texts:
        return []

    embeddings = []

    for text in texts:
        embeddings.append(get_embedding(text))

    return embeddings
