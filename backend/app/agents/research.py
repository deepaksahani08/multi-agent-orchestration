from app.agents.base import BaseAgent
from app.schemas.research import ResearchOutput



class ResearchAgent(BaseAgent):

    prompt_file="research.txt"

    output_schema= ResearchOutput
    