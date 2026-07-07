"""
Evaluation Metrics

Utility functions for calculating evaluation scores.

Responsibilities:
- Calculate overall score
- Assign quality grade
- Determine pass/fail
"""

from app.schemas.evaluation import EvaluationOutput
from app.schemas.evaluation_result import EvaluationMetrics

PASSING_SCORE = 7.0


def calculate_average(evaluation: EvaluationOutput) -> float:
    """
    Calculate the average score across all evaluation metrics.
    """

    scores = [
        evaluation.accuracy.score,
        evaluation.completeness.score,
        evaluation.clarity.score,
        evaluation.relevance.score,
        evaluation.actionability.score,
    ]

    return round(sum(scores) / len(scores), 2)


def get_grade(score: float) -> str:
    """
    Convert a numeric score into a letter grade.
    """

    if score >= 9:
        return "A+"

    if score >= 8:
        return "A"

    if score >= 7:
        return "B"

    if score >= 6:
        return "C"

    return "F"


def is_passing(score: float) -> bool:
    """
    Determine whether the evaluation passes the minimum quality threshold.
    """

    return score >= PASSING_SCORE


def summarize(evaluation: EvaluationOutput) -> dict:
    """
    Return a normalized evaluation summary.
    """

    average = calculate_average(evaluation)

    return EvaluationMetrics(
    average_score=average,
    grade=get_grade(average),
    passed=is_passing(average),
    )