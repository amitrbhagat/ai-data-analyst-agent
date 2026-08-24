from app.rag.ingestion import load_documents
from app.rag.chunking import chunk_text


documents = load_documents("../rag_data/documents")

for document in documents:
    chunks = chunk_text(document["text"])

    print("=" * 70)
    print(f"Source: {document['source_filename']}")
    print(f"Total chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {index + 1}:")
        print(chunk[:500])