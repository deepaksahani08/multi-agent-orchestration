from pydantic import BaseModel, Field


class EvaluationMetric(BaseModel):
    """
    Represents a single evaluation metric.
    """

    score: float = Field(
        ...,
        ge=1,
        le=10,
        description="Score between 1 and 10.",
    )

    feedback: str = Field(
        ...,
        description="Brief explanation for the assigned score.",
    )


class EvaluationOutput(BaseModel):
    """
    Overall report evaluation.
    """

    accuracy: EvaluationMetric

    completeness: EvaluationMetric

    clarity: EvaluationMetric

    relevance: EvaluationMetric

    actionability: EvaluationMetric

    overall_score: float = Field(
        ...,
        ge=1,
        le=10,
        description="Overall quality score.",
    )

    summary: str = Field(
        ...,
        description="Overall evaluation summary.",
    )