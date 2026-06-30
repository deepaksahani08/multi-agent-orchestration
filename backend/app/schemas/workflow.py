from pydantic import BaseModel

from app.agents.planner import PlannerOutput
from app.schemas.research import ResearchOutput


class WorkflowState(BaseModel):
    query:str

    plan:PlannerOutput | None = None

    research: ResearchOutput | None = None

    