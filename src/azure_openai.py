from langchain_openai import AzureChatOpenAI
from .models.ask_input import AskInput


model = AzureChatOpenAI(
    openai_api_version="2023-12-01-preview",
    azure_deployment="gpt-4o-mini",
)


def ask(ask_input: AskInput):
    response = model.invoke(ask_input.text)
    return response
