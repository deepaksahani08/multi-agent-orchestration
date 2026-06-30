from fastapi import APIRouter

from app.core.gemini import llm

router = APIRouter()

@router.get("/test")
def test_llm():

    response = llm.invoke(
        "Say hello in one sentence."
    )

    return {
        "response":response.content
    }