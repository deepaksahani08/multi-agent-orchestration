"""
Workflow State

Every LangGraph node reads from and writes to this shared state.

The state acts as the single source of truth for the entire workflow.
"""

from typing import Any, Dict, List, Optional
from typing_extensions import TypedDict

class WorkflowState(TypedDict):
    """
    The WorkflowState is a dictionary that holds the state of the workflow.

    It is a shared state that is read from and written to by every LangGraph node.
    """

     # Original user prompt
    query: str

     # Planner output
    plan: Optional[Dict[str, Any]]

    # Research output
    research: Optional[Dict[str, Any]]

     # Analysis output
    analysis: Optional[Dict[str, Any]]


      # Final report
    report: Optional[Dict[str, Any]]

     # Evaluation (future)
    evaluation: Optional[Dict[str, Any]]

     # Guardrail results (future)
    guardrail: Optional[Dict[str, Any]]

     # Execution messages/logs
    messages: List[str]