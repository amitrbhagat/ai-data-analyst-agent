from langgraph.graph import StateGraph, START, END
from app.agents.state import State
from app.agents.nodes.question_analyzer import question_analyzer_node
from app.agents.nodes.sql_pipeline_node import sql_pipeline_node
from app.agents.nodes.answer_generator import answer_generator_node
        


builder = StateGraph(State)

builder.add_node("question_analyzer", question_analyzer_node)
builder.add_node("sql_pipeline", sql_pipeline_node)
builder.add_node("answer_generator", answer_generator_node)  


builder.add_edge(START, "question_analyzer")
builder.add_edge("question_analyzer", "sql_pipeline")
builder.add_edge("sql_pipeline", "answer_generator")
builder.add_edge("answer_generator", END)


graph = builder.compile()



if __name__ == "__main__":
    initial_state = {
        "question": "How many customers are there?",
        "conversation_history": [],
        "intent": "SQL",
        "database_schema": "",
        "generated_sql": None,
        "sql_validation_result": None,
        "sql_error": None,
        "query_result": None,
        "retrieved_documents": None,
        "data_summary": None,
        "analysis": None,
        "chart_type": None,
        "chart_config": None,
        "final_answer": None,
        "retry_count": 0,
    }

    result = graph.invoke(initial_state)

    print("\n===== GRAPH RESULT =====")
    print(result)

    