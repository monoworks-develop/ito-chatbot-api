from azure.search.documents.models import VectorizableTextQuery
from fastapi import APIRouter

from src.infrastructure.azure_ai_search import ai_search_client


router = APIRouter(prefix="/azure_ai_search", tags=["azure_ai_search"])


@router.post("/vector_search")
async def aisearch(text: str):
    response = vector_search(text)
    return {"res": response}


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
