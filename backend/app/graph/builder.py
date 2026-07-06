"""
LangGraph Builder

Responsible for building and compiling the workflow graph.

This file only defines the graph structure.

Business logic belongs inside nodes.py
"""

from langgraph.graph import END, START, StateGraph



from app.graph.nodes import (
    guardrail_node,
    planner_node,
    research_node,
    analysis_node,
    report_node,
)

from app.schemas.workflow import WorkflowState
from app.graph.router import workflow_router

def build_graph():
    """ Create and compile the LangGraph workflow."""

    builder = StateGraph(WorkflowState)

    # --------------------------------------------------
    # Register Nodes
    # --------------------------------------------------

    builder.add_node("planner", planner_node)
    builder.add_node("research", research_node)
    builder.add_node("analysis", analysis_node)
    builder.add_node("report", report_node)
    builder.add_node("guardrail", guardrail_node)

     # --------------------------------------------------
    # Define Workflow
    # --------------------------------------------------

    builder.add_edge(START, "guardrail",)

    builder.add_conditional_edges("guardrail", workflow_router,)

    builder.add_edge("planner", "research")

    builder.add_edge("research", "analysis")

    builder.add_edge("analysis", "report")

    builder.add_edge("report", END)


    # --------------------------------------------------
    # Compile
    # --------------------------------------------------


    return builder.compile()
   




# Singleton Graph Instance
graph = build_graph()
