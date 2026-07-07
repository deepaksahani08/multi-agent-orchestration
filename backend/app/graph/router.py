from typing import Literal

from app.graph.constants import PLANNER
from app.schemas.guardrail import GuardrailCategory
from app.schemas.workflow import WorkflowState


def workflow_router(
    state: WorkflowState,
) -> Literal["planner", "__end__"]:
    """
    Route the workflow after the Guardrail node.

    SAFE -> Planner
    Everything else -> END
    """

    if state.guardrail is None:
        return "__end__"

    if state.guardrail.category == GuardrailCategory.SAFE:
        return PLANNER

    return "__end__"