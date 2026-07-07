"""
Evaluation Runner

Coordinates the complete evaluation workflow.

Responsibilities:
- Execute the LLM evaluator
- Calculate evaluation metrics
- Return a unified evaluation result

Future:
- Save evaluation history
- Send results to LangSmith
- Store metrics in MongoDB
- Benchmark prompt versions
"""

from app.evaluation.evaluator import Evaluator
from app.evaluation.metrics import summarize
from app.schemas.evaluation_result import EvaluationResult


class EvaluationRunner:
    """
    Runs the complete evaluation pipeline.
    """

    def __init__(self):
        self.evaluator = Evaluator()

    def evaluate(
        self,
        *,
        query: str,
        report: str,
    ) -> dict:
        """
        Evaluate a generated report.

        Args:
            query: Original user query.
            report: Generated markdown report.

        Returns:
            Dictionary containing:
                - evaluation
                - metrics
        """

        evaluation = self.evaluator.run(
            query=query,
            report=report,
        )

        metrics = summarize(evaluation)

        return EvaluationResult(
            evaluation=evaluation,
            metrics=metrics,
        )


runner = EvaluationRunner()