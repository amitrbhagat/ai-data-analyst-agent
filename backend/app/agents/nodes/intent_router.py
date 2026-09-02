from app.agents.state import State
from app.services.routing_service import classify_intent


def intent_router_node(state: State) -> dict:

    question = state["question"]

    result = classify_intent(question)

    return {
        "intent": result.route
    }
