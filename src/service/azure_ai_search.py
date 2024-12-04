from azure.search.documents.models import VectorizableTextQuery

from src.infrastructure.azure.ai_search.client import ai_search_client


def vector_search(text: str):
    # MEMO: 対象のIndexにVectorizerが設定されている場合はVectorizableTextQueryを使用できます。
    #       これを使用することで渡されたtextを自動的にベクトル変換してベクトル検索が行えます。
    #       これを使用しない場合は自分でベクトルを生成する処理が必要になります。
    vector_query = VectorizableTextQuery(
        text=text,
        fields="weather_vector,date_vector",
        exhaustive=False,
    )
    # テキストとベクトルのハイブリッド検索
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
