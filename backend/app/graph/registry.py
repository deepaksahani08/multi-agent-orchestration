"""
Graph Registry

Responsible for registering nodes and edges.

This keeps builder.py small and easy to maintain.
"""

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    analysis_node,
    evaluation_node,
    guardrail_node,
    planner_node,
    report_node,
    research_node,
)

from app.graph.constants import (
    ANALYSIS,
    EVALUATION,
    GUARDRAIL,
    PLANNER,
    REPORT,
    RESEARCH,
)

from app.graph.router import workflow_router


def register_nodes(builder: StateGraph):
    """
    Register all graph nodes.
    """

    builder.add_node(GUARDRAIL, guardrail_node)
    builder.add_node(PLANNER, planner_node)
    builder.add_node(RESEARCH, research_node)
    builder.add_node(ANALYSIS, analysis_node)
    builder.add_node(REPORT, report_node)
    builder.add_node(EVALUATION, evaluation_node)


def register_edges(builder: StateGraph):

    builder.add_edge( START,  GUARDRAIL,)

    builder.add_conditional_edges(GUARDRAIL, workflow_router,)

    builder.add_edge(PLANNER,RESEARCH,)

    builder.add_edge( RESEARCH, ANALYSIS,)

    builder.add_edge(ANALYSIS,REPORT,)

    builder.add_edge(REPORT,EVALUATION,)

    builder.add_edge(EVALUATION, END,)