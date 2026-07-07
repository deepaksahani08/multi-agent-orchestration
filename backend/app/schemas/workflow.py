from pydantic import BaseModel, Field

from app.schemas.agent import AgentStatus
from app.schemas.analysis import AnalysisOutput
from app.schemas.planner import PlannerOutput
from app.schemas.research import ResearchOutput
from app.schemas.report import ReportOutput
from app.schemas.guardrail import GuardrailOutput
from app.schemas.evaluation_result import EvaluationResult



class WorkflowState(BaseModel):
    query: str

    guardrail: GuardrailOutput | None = None

    plan: PlannerOutput | None = None

    research: ResearchOutput | None = None

    analysis: AnalysisOutput | None = None

    report: ReportOutput | None = None
    
    evaluation: EvaluationResult | None = None



    agent_status: list[AgentStatus] = Field(default_factory=list)