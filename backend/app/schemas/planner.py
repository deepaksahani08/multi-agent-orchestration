from pydantic import BaseModel, Field


class PlannerOutput(BaseModel):
    goal:str = Field(
        description="Main objective of the user request."
    ) 

    tasks:list[str] = Field(
        description="ordered execution plan."
    ) 