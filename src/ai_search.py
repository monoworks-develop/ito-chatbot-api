from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery

from .config import get_settings


async def ai_search(text: str):
    settings = get_settings()
    service_endpoint = settings.AZURE_SEARCH_SERVICE_ENDPOINT
    index_name = settings.AZURE_SEARCH_INDEX_NAME
    key = settings.AZURE_SEARCH_API_KEY
    credential = AzureKeyCredential(key)

    search_client = SearchClient(service_endpoint, index_name, credential)

    vector_query = VectorizableTextQuery(
        text=text, fields="weather_vector,date_vector", exhaustive=False
    )

    results = search_client.search(
        search_text=text,
        vector_queries=[vector_query],
        select=["place", "date", "weather"],
        top=10,
    )

    response = []
    for result in results:
        print("{}: {})".format(result["date"], result["weather"]))
        response.append({"date": result["date"], "weather": result["weather"]})

    return response
