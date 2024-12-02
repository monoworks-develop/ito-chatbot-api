from fastapi import FastAPI

from .config import get_settings

from .models.ask_input import AskInput

from .azure_openai import ask

app = FastAPI()


@app.get("/")
def read_root():
    settings = get_settings()
    return {"message": "Hello World", "endpoint": settings.AZURE_OPENAI_ENDPOINT}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/ask")
async def ask_model(ask_input: AskInput):
    res = ask(ask_input)
    return {"res": res}
