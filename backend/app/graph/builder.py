"""
LangGraph Builder

Builds and compiles the workflow graph.
"""

from langgraph.graph import StateGraph

from app.graph.registry import (
    register_edges,
    register_nodes,
)
from app.schemas.workflow import WorkflowState


def build_graph():
    """
    Build and compile the workflow graph.
    """

    builder = StateGraph(WorkflowState)

    register_nodes(builder)

    register_edges(builder)

    return builder.compile()


graph = build_graph()