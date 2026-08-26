from app.rag.ingestion import load_documents
from app.rag.chunking import chunk_text
from app.rag.embeddings import get_embeddings
from app.rag.vector_store import add_documents, query_documents
from app.llm.ollama import generate_embedding


# --------------------------------------------------
# 1. Load documents
# --------------------------------------------------

documents = load_documents("../rag_data/documents")


# --------------------------------------------------
# 2. Create chunks and store embeddings
# --------------------------------------------------

for document in documents:

    chunks = chunk_text(document["text"])

    embeddings = get_embeddings(chunks)

    add_documents(
        chunks=chunks,
        embeddings=embeddings,
        source_filename=document["source_filename"],
    )

    print(
        f"Stored {len(chunks)} chunks from "
        f"{document['source_filename']}"
    )


# --------------------------------------------------
# 3. Create query embedding
# --------------------------------------------------

question = "How long do I have to request a refund?"

query_embedding = generate_embedding(question)


# --------------------------------------------------
# 4. Search ChromaDB
# --------------------------------------------------

results = query_documents(
    query_embedding=query_embedding,
    n_results=3,
)


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

print("\n" + "=" * 70)
print("SEARCH RESULTS")
print("=" * 70)

for index, result in enumerate(results, start=1):

    print(f"\nResult {index}")

    print(
        f"Source: "
        f"{result['metadata']['source_filename']}"
    )

    print(
        f"Chunk: "
        f"{result['metadata']['chunk_index']}"
    )

    print(
        f"Distance: "
        f"{result['distance']}"
    )

    print(f"Text:\n{result['text']}")

    