from app.agents.planner import PlannerAgent
from app.agents.research import ResearchAgent
from app.schemas.workflow import WorkflowState


class Workflow:

    def __init__(self):

        self.planner = PlannerAgent()

        self.research = ResearchAgent()

    def invoke(self, query: str) -> WorkflowState:

        state = WorkflowState(
            query=query
        )

        state.plan = self.planner.run(
            query=query
        )

        state.research = self.research.run(
            goal=state.plan.goal,
            tasks="\n".join(state.plan.tasks),
        )

        return state