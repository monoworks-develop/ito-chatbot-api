from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controller.router import api_router

app = FastAPI()

origins = ["http://localhost:3000", "https://ito-chatbot-ui.azurewebsites.net:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(router=api_router)
