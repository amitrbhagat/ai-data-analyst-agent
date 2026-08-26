from app.rag.retrieval import retrieve_relevant_chunks


question = "What is the refund period for an eligible product?"

results = retrieve_relevant_chunks(
    question,
    top_k=3,
    distance_threshold = 3.0
)

print("\n===== RETRIEVAL RESULTS =====\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}")
    print(f"Source: {result['source_filename']}")
    print(f"Distance: {result['distance']}")
    print(f"Text: {result['text']}")
    print("-" * 60)
    