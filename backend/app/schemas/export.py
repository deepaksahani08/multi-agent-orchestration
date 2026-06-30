from pydantic import BaseModel, Field


class ExportRequest(BaseModel):
    markdown: str = Field(
        min_length=1,
        description="Markdown report to export."
    )