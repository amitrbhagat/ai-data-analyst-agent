from langgraph.graph import StateGraph, START, END

from app.agents.state import State

from app.agents.nodes.question_analyzer import question_analyzer_node
from app.agents.nodes.intent_router import intent_router_node
from app.agents.nodes.sql_pipeline_node import sql_pipeline_node
from app.agents.nodes.rag_retriever import rag_retriever_node
from app.agents.nodes.synthesis import synthesis_node
from app.agents.nodes.answer_generator import answer_generator_node


def route_intent(state: State) -> str:
    intent = state["intent"].upper()

    if intent == "SQL":
        return "sql"

    if intent == "RAG":
        return "rag"

    if intent == "HYBRID":
        return "hybrid"

    raise ValueError(f"Invalid intent: {intent}")


def route_after_sql(state: State) -> str:
    intent = state["intent"].upper()

    if intent == "HYBRID":
        return "rag"

    return "answer"


def route_after_rag(state: State) -> str:
    intent = state["intent"].upper()

    if intent == "HYBRID":
        return "synthesis"

    return "answer"


builder = StateGraph(State)


# -----------------------------
# Add Nodes
# -----------------------------

builder.add_node(
    "question_analyzer",
    question_analyzer_node
)

builder.add_node(
    "intent_router",
    intent_router_node
)

builder.add_node(
    "sql_pipeline",
    sql_pipeline_node
)

builder.add_node(
    "rag_retriever",
    rag_retriever_node
)

builder.add_node(
    "synthesis",
    synthesis_node
)

builder.add_node(
    "answer_generator",
    answer_generator_node
)


# -----------------------------
# Initial Flow
# -----------------------------

builder.add_edge(
    START,
    "question_analyzer"
)

builder.add_edge(
    "question_analyzer",
    "intent_router"
)


# -----------------------------
# Intent Routing
# -----------------------------

builder.add_conditional_edges(
    "intent_router",
    route_intent,
    {
        "sql": "sql_pipeline",
        "rag": "rag_retriever",
        "hybrid": "sql_pipeline",
    },
)


# -----------------------------
# SQL Routing
# -----------------------------

builder.add_conditional_edges(
    "sql_pipeline",
    route_after_sql,
    {
        "rag": "rag_retriever",
        "answer": "answer_generator",
    },
)


# -----------------------------
# RAG Routing
# -----------------------------

builder.add_conditional_edges(
    "rag_retriever",
    route_after_rag,
    {
        "synthesis": "synthesis",
        "answer": "answer_generator",
    },
)


# -----------------------------
# Hybrid Synthesis
# -----------------------------

builder.add_edge(
    "synthesis",
    "answer_generator"
)


# -----------------------------
# Final
# -----------------------------

builder.add_edge(
    "answer_generator",
    END
)


graph = builder.compile()
