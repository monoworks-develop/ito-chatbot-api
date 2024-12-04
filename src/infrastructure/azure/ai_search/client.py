from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from src.core.config import settings


# AI Searchのクライアント
def create_azure_ai_search_client():
    service_endpoint = settings.AZURE_SEARCH_SERVICE_ENDPOINT
    index_name = settings.AZURE_SEARCH_INDEX_NAME
    key = settings.AZURE_SEARCH_API_KEY
    credential = AzureKeyCredential(key)

    ai_search_client = SearchClient(service_endpoint, index_name, credential)
    return ai_search_client


# インスタンス化
ai_search_client = create_azure_ai_search_client()
