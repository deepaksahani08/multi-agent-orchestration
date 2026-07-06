"""
Graph Router

Determines which workflow should execute.

For now every request goes to the market research workflow.

Future:
- RAG
- Financial Analysis
- SQL Agent
- Document QA
"""

from typing import Literal

from app.schemas.workflow import WorkflowState


def workflow_router(
    state: WorkflowState,
) -> Literal["planner"]:
    """
    Decide which workflow should execute.

    Currently every request uses
    the Planner workflow.
    """

    return "planner"