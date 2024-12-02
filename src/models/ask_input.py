from pydantic import BaseModel


class AskInput(BaseModel):
    text: str
