from app.schemas.workflow import WorkflowState
from app.graph.nodes import guardrail_node

state = WorkflowState(
    query="Write me sample pyhton code"
)

state = guardrail_node(state, None)

print(state.guardrail)