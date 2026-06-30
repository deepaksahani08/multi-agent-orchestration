from fastapi import APIRouter

from app.agents.planner import PlannerAgent

from app.schemas.request import PlannerRequest
from app.core.workflow import Workflow


router = APIRouter()


planner = PlannerAgent()

workflow = Workflow()

@router.post("/planner")
def planner_route(request: PlannerRequest):

    result = planner.run(
        query = request.query
    )

    return result.model_dump()


#workflow


@router.post("/generate")
async def generate(request: PlannerRequest):

    result = workflow.invoke(
        request.query
    )

    return result.model_dump()



#workflow new
# from fastapi import APIRouter

# from app.core.workflow import Workflow
# from app.schemas.request import PlannerRequest

# router = APIRouter()

# workflow = Workflow()


# @router.post("/generate")
# async def generate(request: PlannerRequest):

#     result = workflow.invoke(
#         request.query
#     )

#     return result.model_dump()