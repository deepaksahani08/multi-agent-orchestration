from app.agents.base import BaseAgent
from app.schemas.guardrail import GuardrailOutput


class GuardrailAgent(BaseAgent):
    """
    AI Guardrail Agent

    Classifies whether a user's request is safe
    to enter the Market Research workflow.
    """

    prompt_file = "guardrail.md"

    output_schema = GuardrailOutput