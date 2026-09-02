from app.services.routing_service import classify_intent


test_questions = [
    # -------------------------
    # SQL QUESTIONS
    # -------------------------
    {
        "question": "How many customers do we have?",
        "expected": "SQL"
    },
    {
        "question": "What was our total revenue last month?",
        "expected": "SQL"
    },
    {
        "question": "What are the top 5 products by sales?",
        "expected": "SQL"
    },
    {
        "question": "How many orders were placed in each region?",
        "expected": "SQL"
    },
    {
        "question": "Which product generated the highest revenue?",
        "expected": "SQL"
    },

    # -------------------------
    # RAG QUESTIONS
    # -------------------------
    {
        "question": "What is the refund policy?",
        "expected": "RAG"
    },
    {
        "question": "How long do I have to request a refund?",
        "expected": "RAG"
    },
    {
        "question": "How can I contact customer support?",
        "expected": "RAG"
    },
    {
        "question": "What is the warranty period for electronics?",
        "expected": "RAG"
    },
    {
        "question": "What happens when a package is returned to the sender?",
        "expected": "RAG"
    },

    # -------------------------
    # HYBRID QUESTIONS
    # -------------------------
    {
        "question": "What are our top 5 products by sales, and does the refund policy cover them?",
        "expected": "HYBRID"
    },
    {
        "question": "How many electronics were sold last year, and what is their warranty period?",
        "expected": "HYBRID"
    },
    {
        "question": "Which region had the most orders, and what are the shipping rules for that region?",
        "expected": "HYBRID"
    },

    # -------------------------
    # AMBIGUOUS / TRICKY
    # -------------------------
    {
        "question": "Tell me about our products.",
        "expected": "RAG"
    },
    {
        "question": "What are our best products?",
        "expected": "SQL"
    },
]


def main():
    total = len(test_questions)
    correct = 0

    print("=" * 70)
    print("DAY 10 - INTENT ROUTING TEST")
    print("=" * 70)

    for index, test in enumerate(test_questions, start=1):

        question = test["question"]
        expected = test["expected"]

        print(f"\nTest {index}/{total}")
        print(f"Question : {question}")
        print(f"Expected : {expected}")

        try:
            result = classify_intent(question)

            actual = result.route

            print(f"Actual   : {actual}")
            print(f"Reason   : {result.reasoning}")
            print(f"Confidence: {result.confidence}")

            if actual == expected:
                print("Result   : PASS")
                correct += 1
            else:
                print("Result   : FAIL")

        except Exception as e:
            print(f"Result   : ERROR")
            print(f"Error    : {e}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"Total tests : {total}")
    print(f"Passed      : {correct}")
    print(f"Failed      : {total - correct}")

    accuracy = (correct / total) * 100

    print(f"Accuracy    : {accuracy:.2f}%")
    print("=" * 70)


if __name__ == "__main__":
    main()