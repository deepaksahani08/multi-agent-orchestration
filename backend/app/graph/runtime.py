"""
Graph Runtime

Responsible for executing the compiled LangGraph.

This layer isolates execution concerns from graph construction.

Future responsibilities:

- LangSmith tracing
- Streaming
- Checkpointing
- Retry policies
- Human approval
- Metrics
- Logging
"""

from app.graph.builder import graph
from app.schemas.workflow import WorkflowState


class GraphRuntime:
    """
    Executes the LangGraph workflow.
    """

    def invoke(
        self,
        state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the workflow synchronously.

        Args:
            state: Initial workflow state.

        Returns:
            Updated workflow state.
        """

        result = graph.invoke(state)

        return WorkflowState.model_validate(result)


# Singleton Runtime
runtime = GraphRuntime()