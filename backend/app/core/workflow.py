from app.agents.analysis import AnalysisAgent
from app.agents.planner import PlannerAgent
from app.agents.research import ResearchAgent
from app.schemas.workflow import WorkflowState


class Workflow:

    def __init__(self):
        self.planner = PlannerAgent()
        self.research = ResearchAgent()
        self.analysis = AnalysisAgent()

    def invoke(self, query: str) -> WorkflowState:

        state = WorkflowState(query=query)

        state.plan = self.planner.run(query=query)

        state.research = self.research.run(
            goal=state.plan.goal,
            tasks="\n".join(state.plan.tasks),
        )

        state.analysis = self.analysis.run(
            summary=state.research.summary,
            findings="\n".join(state.research.findings),
        )

        return state