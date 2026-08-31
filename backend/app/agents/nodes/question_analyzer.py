from app.agents.state import State
from app.database.schema import get_schema_description


def question_analyzer_node(state: State) -> dict:

    return {
        "question": state["question"],
        "database_schema": get_schema_description(),
    }
