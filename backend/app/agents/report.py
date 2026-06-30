from app.agents.base import BaseAgent
from app.schemas.report import ReportOutput



class ReportAgent(BaseAgent):

    prompt_file = "report.txt"

    output_schema = ReportOutput
