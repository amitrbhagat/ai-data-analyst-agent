from app.rag.ingestion import load_documents


documents = load_documents("C:/Users/Hp/Desktop/AI Engineer/ai-data-analyst-agent/rag_data/documents")

print(f"Loaded {len(documents)} documents")


for document in documents:
    print("=" * 60)
    print(f"source: {document['source_filename']}")
    print(f"Characters: {len(document['text'])}")
    print(document["text"][:500])
    print()
