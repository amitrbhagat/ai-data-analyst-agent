from app.rag.embeddings import get_embeddings
from app.rag.ingestion import load_documents
from app.rag.chunking import chunk_text


# text = "Customers can request a refund within 30 days of delivery."


# embeddings = get_embedding(text)

# print("Embedding generated successfully.")
# print(f"Vector dimensions: {len(embeddings)}")
# print(f"First 10 values: {embeddings[:10]}")


documents = load_documents("../rag_data/documents")

for document in documents:

    chunks = chunk_text(document["text"])

    embeddings = get_embeddings(chunks)

    print("=" * 60)
    print(f"Source: {document['source_filename']}")
    print(f"Chunks: {len(chunks)}")
    print(f"Embeddings: {len(embeddings)}")

    if embeddings:
        print(f"Vector dimensions: {len(embeddings[0])}")
