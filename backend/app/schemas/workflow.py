from pydantic import BaseModel, Field

from app.schemas.agent import AgentStatus
from app.schemas.analysis import AnalysisOutput
from app.schemas.planner import PlannerOutput
from app.schemas.research import ResearchOutput


class WorkflowState(BaseModel):
    query: str

    plan: PlannerOutput | None = None

    research: ResearchOutput | None = None

    analysis: AnalysisOutput | None = None

    agent_status: list[AgentStatus] = Field(default_factory=list)