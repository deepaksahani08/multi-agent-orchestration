from typing import Literal

from pydantic import BaseModel


class AgentStatus(BaseModel):
    name: str
    status: Literal["pending", "running", "completed", "failed"]
    duration_ms: int | None = None