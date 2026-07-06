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

from app.schemas.guardrail import GuardrailCategory
from app.schemas.workflow import WorkflowState


def workflow_router(
    state: WorkflowState,
) -> Literal["planner", "__end__"]:

    if state.guardrail is None:
        return "__end__"

    if state.guardrail.category == GuardrailCategory.SAFE:
        return "planner"

    return "__end__"