from fastapi import APIRouter

from app.agents.planner import PlannerAgent
from app.schemas.request import PlannerRequest


router = APIRouter()


planner = PlannerAgent()



@router.post("/planner")
def planner_route(request: PlannerRequest):

    result = planner.run(
        query = request.query
    )

    return result.model_dump()