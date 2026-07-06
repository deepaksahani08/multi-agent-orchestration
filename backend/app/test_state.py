from app.graph.state import WorkflowState

state:WorkflowState = {
    "query": "Create NVIDIA report",
    "plan": None,
    "research": None,
    "analysis": None,
    "report": None,
    "evaluation": None,
    "guardrail": None,
    "messages": []
}

print(state)