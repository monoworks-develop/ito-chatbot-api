from fastapi import APIRouter

from src.models import AskInput
from src.service.azure_openai import ask

router = APIRouter()


@router.post("/azure_openai/ask", tags=["azure_openai"])
def post_ask(ask_input: AskInput):
    res = ask(ask_input)
    return {"res": res}
