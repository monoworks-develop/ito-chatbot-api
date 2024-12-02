from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str


@lru_cache()
def get_settings():
    return Settings()
