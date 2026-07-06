"""
Workflow Service

Acts as the orchestration layer between the API and LangGraph.
"""
from uuid import uuid4
from langchain_core.runnables import RunnableConfig
from app.graph.runtime import runtime
from app.schemas.workflow import WorkflowState



class Workflow:
    """
    Public workflow service used by the API.
    """

    def invoke(
        self,
        query: str,
    ) -> WorkflowState:

        initial_state = WorkflowState(
            query=query,
        )

        config: RunnableConfig = {
            "run_name": "Market Research Workflow",
            "run_id": uuid4(),
            "tags": [
                "langgraph",
                "market-research",
                "production",
            ],
            
             "metadata": {
                "workflow": "market-research",
                "version": "1.0.0",
            },
        }

        return runtime.invoke(
            state=initial_state,
            config=config,
        )

