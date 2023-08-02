from pydantic import BaseModel


class PingPongRequestBody(BaseModel):
    song: str
    name: str


class AuthRequestBody(BaseModel):
    access_id: str
    access_key: str


class TwiceRequestBody(BaseModel):
    number: int
