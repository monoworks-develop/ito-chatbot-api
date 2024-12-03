from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str

    AZURE_SEARCH_SERVICE_ENDPOINT: str
    AZURE_SEARCH_INDEX_NAME: str
    AZURE_SEARCH_API_KEY: str


@lru_cache()
def get_settings():
    return Settings()
