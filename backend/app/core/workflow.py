"""
Workflow Service

Acts as the orchestration layer between the API and LangGraph.

The API should never call LangGraph directly.

If the orchestration engine changes in the future,
only this file needs to change.
"""

from app.graph.builder import graph
from app.schemas.workflow import WorkflowState


class Workflow:
    """
    Workflow wrapper around LangGraph.
    """

    def invoke(self, query: str) -> WorkflowState:
        """
        Execute the LangGraph workflow.

        Args:
            query: User prompt.

        Returns:
            WorkflowState
        """

        initial_state = WorkflowState(
            query=query,
        )

        result = graph.invoke(initial_state)

        return WorkflowState.model_validate(result)