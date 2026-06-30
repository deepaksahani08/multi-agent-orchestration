from pydantic import BaseModel, Field



class ReportOutput(BaseModel):

    markdown:str= Field(
        description="Final report in Markdown format."
    )