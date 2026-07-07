from pydantic import BaseModel

from app.schemas.evaluation import EvaluationOutput


class EvaluationMetrics(BaseModel):
    average_score: float
    grade: str
    passed: bool


class EvaluationResult(BaseModel):
    """
    Final evaluation returned by the Evaluation Runner.
    """

    evaluation: EvaluationOutput

    metrics: EvaluationMetrics