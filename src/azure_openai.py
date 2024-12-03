from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from .models.ask_input import AskInput


chat_model = AzureChatOpenAI(
    openai_api_version="2023-12-01-preview",
    azure_deployment="gpt-4o-mini",
)

embedding_model = AzureOpenAIEmbeddings(
    openai_api_version="2023-12-01-preview", model="text-embedding-3-small"
)


def ask(ask_input: AskInput):
    response = chat_model.invoke(ask_input.text)
    return response


# def generate_embedding(text):
#     single_vector = embedding_model.aembed_query(text)
#     return single_vector
