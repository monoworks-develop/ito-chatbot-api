from fastapi import APIRouter


from src.controllers import azure_ai_search, azure_openai


api_router = APIRouter()

api_router.include_router(azure_ai_search.router)
api_router.include_router(azure_openai.router)
