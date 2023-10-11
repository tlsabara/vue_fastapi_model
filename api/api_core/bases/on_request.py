from pydantic import BaseModel


class PingPongRequestBody(BaseModel):
    """Apenas um body de teste e deve ser apagado
    """
    song: str
    name: str


class AuthRequestBody(BaseModel):
    """This is the body of authentication request
    """
    access_id: str
    access_key: str


class TwiceRequestBody(BaseModel):
    """Only another test, shold be deleted(in the future)
    """
    number: int
