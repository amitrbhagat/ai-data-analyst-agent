from typing import TypedDict, Optional, Any


class State(TypedDict):

    question: str
    conversation_history = list
    intent:str
    database_schema:str

    generated_sql:Optional[str]
    sql_validation_result: Optional[str]
    sql_error:Optional[str]
    query_result:Optional[str]

    retrieved_documents:Optional[list]
    rag_answer: str|None
    synthesis_answer: str|None


    data_summary:Optional[str]
    analysis:Optional[dict]

    chart_type:Optional[str]
    chart_config:Optional[dict]

    final_answer = Optional[str]

    retry_count: int
