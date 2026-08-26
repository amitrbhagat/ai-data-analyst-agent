import chromadb
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parents[3]
CHROMA_PATH = BASE_DIR / "rag_data" / "processed" / "chroma_db"

COLLECTION_NAME = "policy_documents"



def get_vector_store():

    CHROMA_PATH.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(
        path=str(CHROMA_PATH)
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME 
    )

    return collection  



def add_documents(
    chunks: list[str],
    embeddings: list[list[float]],
    metadatas: list[dict],
    ids: list[str],
):
    collection = get_vector_store()

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )




def query_documents(query_embedding: list[float], n_results: int = 5,):

    collection = get_vector_store()

    if collection.count() == 0:
        return []

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

    matches = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for document, metadata, distance in zip(documents, metadatas, distances):

        matches.append(
            {
                "text": document,
                "metadata": metadata,
                "distance": distance,
            }
        )

    return matches         
        