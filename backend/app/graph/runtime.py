"""
Graph Runtime

Responsible for executing the compiled LangGraph.

Future responsibilities:
- LangSmith tracing
- Streaming
- Checkpointing
- Retry
- Human approval
"""

from langchain_core.runnables import RunnableConfig

from app.graph.builder import graph
from app.schemas.workflow import WorkflowState


class GraphRuntime:
    """
    Executes the compiled LangGraph.
    """

    def invoke(
        self,
        state: WorkflowState,
        config: RunnableConfig | None = None,
    ) -> WorkflowState:
        """
        Execute the workflow.

        Args:
            state: Initial workflow state.
            config: Optional LangGraph execution configuration.

        Returns:
            WorkflowState
        """

    

        result = graph.invoke(
            input=state,
            config=config,
        )

    
        return WorkflowState.model_validate(result)


runtime = GraphRuntime()