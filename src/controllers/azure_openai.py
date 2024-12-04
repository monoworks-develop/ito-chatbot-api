from fastapi import APIRouter
from src.models import AskInput
from src.infrastructure.azure_openai import openai_chat_model


router = APIRouter(prefix="/azure_openai", tags=["azure_openai"])


@router.post("/ask")
async def ask_model(ask_input: AskInput):
    res = ask(ask_input)
    return {"res": res}


def ask(ask_input: AskInput):
    response = openai_chat_model.invoke(ask_input.text)
    return response
