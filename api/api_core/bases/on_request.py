from pydantic import BaseModel


class PingPongRequestBody(BaseModel):
    song: str
    name: str
