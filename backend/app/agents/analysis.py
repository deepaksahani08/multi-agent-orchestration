from app.agents.base import BaseAgent
from app.schemas.analysis import AnalysisOutput


class AnalysisAgent(BaseAgent):
    prompt_file = "analysis.txt"

    output_schema = AnalysisOutput