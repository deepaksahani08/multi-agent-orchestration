"""
LLM-as-a-Judge Evaluator

Evaluates the quality of AI-generated market research reports.

Responsibilities:
- Score report quality
- Provide structured feedback
- Support automated evaluation
"""

from app.agents.base import BaseAgent
from app.schemas.evaluation import EvaluationOutput


class Evaluator(BaseAgent):
    """
    LLM-as-a-Judge evaluator.

    Uses Gemini to evaluate the generated report against
    a predefined rubric.
    """ 

    prompt_file = "evaluator.md"

    output_schema = EvaluationOutput