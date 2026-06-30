from pydantic import BaseModel, Field



class AnalysisOutput(BaseModel):

    insights:list[str] = Field(
        description="key insights derived from the research."
    )

    trends:list[str] = Field(
        description="Current market trends."
    )

    opportunities: list[str] = Field(
        description="Business opportunities."
    )

    risks:list[str] = Field(
        description="Potential risks and challenges."
    )

    recommendations: list[str] = Field(
        description="Recommended actions."
    )
