from fastapi import FastAPI

from src.controller.router import api_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(router=api_router)
