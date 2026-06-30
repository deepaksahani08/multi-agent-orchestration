from app.agents.base import BaseAgent
from app.schemas.planner import PlannerOutput



class PlannerAgent(BaseAgent):

    prompt_file = "planner.txt"

    output_schema = PlannerOutput

    
