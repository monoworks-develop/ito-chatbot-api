from src.infrastructure.azure.openai.model import openai_chat_model
from src.models import AskInput


def ask(ask_input: AskInput):
    response = openai_chat_model.invoke(ask_input.text)
    return response
