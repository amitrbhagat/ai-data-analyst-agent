from app.rag.embeddings import get_embedding
from app.rag.vector_store import get_vector_store


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 3,
    distance_threshold: float = 3.0,
) -> list[dict]:
    """
    Retrieve the most relevant policy chunks for a user query.
    """

    query_embedding = get_embedding(query)

    collection = get_vector_store()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    retrieved_chunks = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        
        if distance > distance_threshold:
            continue

        retrieved_chunks.append(
            {
                "text": document,
                "source_filename": metadata.get(
                    "source_filename"
                ),
                "distance": distance,
            }
        )

    return retrieved_chunks
