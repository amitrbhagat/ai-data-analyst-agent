from app.agents.state import State
from app.services.sql_service import generate_and_execute_sql
from app.services.chart_service import decide_chart




def sql_pipeline_node(state: State) -> dict:
    print("[NODE] sql_pipeline")

    question = state["question"]

    result = generate_and_execute_sql(question, 1)

    if result["success"]:

        query_result = (
            result["dataframe"].to_dict(orient = "records")
            if result["dataframe"] is not None
            else None
        )

        chart = decide_chart(query_result)

        return {
            "generated_sql": result["final_sql"],
            "query_result": query_result,
            "chart_type": chart["chart_type"],
            "chart_config": {
                "x": chart["x"],
                "y": chart["y"],
            },
            "sql_error": None,
            "retry_count": result["attempts"] - 1,
        }
    
    return {
        "generated_sql":result.get("final_sql"),
        "query_result":None,
        "sql_error":result.get("error_message"),
        "retry_count":result.get("attempts", 1) - 1,
    }
