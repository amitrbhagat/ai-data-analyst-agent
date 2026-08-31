from app.services.rag_service import answer_from_documents


def test_question(question: str):
    print("\n" + "=" * 70)
    print(f"QUESTION: {question}")
    print("=" * 70)

    result = answer_from_documents(question)

    print("\nANSWER:")
    print(result.answer)

    print("\nSOURCES:")
    print(result.sources)

    print("\nGROUNDED:")
    print(result.grounded)

    print("\nCONFIDENCE:")
    print(result.confidence)


if __name__ == "__main__":

    test_question(
        "What is the refund policy?"
    )

    # In-scope question
    test_question(
        "How long is the warranty for electronics?"
    )

    # Another in-scope question
    test_question(
        "What is the refund period?"
    )

    # Clearly out-of-scope question
    test_question(
        "What is the weather today?"
    )