from app.agents.graph import graph


initial_state = {
    "question": "How many customers do we have?",
    "conversation_history": [],
    "intent": "",
    "database_schema": "",

    "generated_sql": None,
    "sql_validation_result": None,
    "sql_error": None,
    "query_result": None,
    "retry_count": 0,

    "retrieved_documents": None,
    "rag_answer": None,

    "hybrid_answer": None,

    "data_summary": None,
    "analysis": None,
    "chart_type": None,
    "chart_config": None,
    "final_answer": None,
}


result = graph.invoke(initial_state)

print("Intent:", result["intent"])
print("Result keys:", result.keys())
print("Final Answer:", result.get("final_answer"))

