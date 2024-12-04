from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings


# チャットモデル
def create_azure_openai_chat_model(azure_deployment: str):
    openai_chat_model = AzureChatOpenAI(azure_deployment=azure_deployment)
    return openai_chat_model


# 埋め込みモデル
def create_azure_openai_embedding_model(model: str):
    openai_embedding_model = AzureOpenAIEmbeddings(model=model)
    return openai_embedding_model


# インスタンス化
openai_chat_model = create_azure_openai_chat_model("gpt-4o-mini")
# openai_embedding_model = create_azure_openai_embedding_model("text-embedding-3-small")
