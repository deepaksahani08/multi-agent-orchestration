from pydantic import BaseModel, Field



class ResearchOutput(BaseModel):

    summary:str = Field(
        description="Overall reasearch summary."
    )

    findings:list[str] = Field(
        description="Important research findings"
    )

    sources: list[str] = Field(
        description="Refrence sources used."
    )