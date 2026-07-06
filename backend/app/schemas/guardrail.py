from enum import Enum

from pydantic import BaseModel, Field

class GuardrailCategory(str, Enum):
    SAFE = "SAFE"
    PROMPT_INJECTION = "PROMPT_INJECTION"
    JAILBREAK = "JAILBREAK"
    IRRELEVANT = "IRRELEVANT"
    HARMFUL = "HARMFUL"


class GuardrailOutput(BaseModel):
    """
    Output produced by the Guardrail Agent.

    The agent classifies whether the user's request
    is safe to process by the workflow.
    """

    safe: bool = Field(
        ...,
        description="Whether the request is safe to continue.",
    )

    category: GuardrailCategory = Field(
        ...,
        description="Classification of the request.",
    )

    reason: str = Field(
        ...,
        description="Short explanation for the decision.",
    )