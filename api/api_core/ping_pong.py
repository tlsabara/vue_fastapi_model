import os
from pydantic import BaseModel


class PingPongResponse(BaseModel):
    word: str


async def route_post(body_request:PingPongResponse):
    """Função rota de post do ping pong, com parâmetros não obrigatórios
    """

    return {"message": "PONG", "method": "POST", 'word': body_request.word, "version": os.environ.get('API_VERSION')}


async def route_get(word=None):
    """Função para a rota de get do ping pong, com parâmetros não obrigatórios
    """
    dict_1 = {"message": "PONG", "method": "GET", "version": os.environ.get('API_VERSION')}
    return dict_1 if not word else {"message": "PONG", "method": "GET", "word": word,
                                    "version": os.environ.get('API_VERSION')}


async def route_put():
    """Função para a rota de put do ping pong, sem parâmetros
    """
    return {"message": "PONG", "method": "PUT", "version": os.environ.get('API_VERSION')}


async def route_delete():
    """Função para a rota de delete do ping pong, sem parâmetros
    """
    return {"message": "PONG", "method": "DELETE", "version": os.environ.get('API_VERSION')}
