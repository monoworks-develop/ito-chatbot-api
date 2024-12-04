from fastapi import APIRouter

from src.service.azure_ai_search import vector_search

router = APIRouter(prefix="/azure_ai_search", tags=["azure_ai_search"])


@router.post("/vector_search")
def post_vector_search(text: str):
    response = vector_search(text)
    return {"res": response}
