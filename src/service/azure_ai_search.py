from azure.search.documents.models import VectorizableTextQuery

from src.infrastructure.azure.ai_search.client import ai_search_client


def vector_search(text: str):
    vector_query = VectorizableTextQuery(
        text=text,
        k_nearest_neighbors=5,
        fields="weather_vector,date_vector",
        exhaustive=False,
    )

    search_results = ai_search_client.search(
        search_text=text,
        vector_queries=[vector_query],
        select=["place", "date", "weather"],
        top=5,
    )

    response = []
    for result in search_results:
        response.append(
            {
                "place": result["place"],
                "date": result["date"],
                "weather": result["weather"],
            }
        )

    return response
