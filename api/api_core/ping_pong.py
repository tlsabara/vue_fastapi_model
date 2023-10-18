from random import randint

from fastapi import Response, status

from api.api_core.bases.on_request import PingPongRequestBody
from api.api_core.bases.on_response import DefaulApiResponse


async def route_post(response: Response, body_request: PingPongRequestBody) -> DefaulApiResponse:
    """Função rota de post do ping pong, com parâmetros não obrigatórios, mas com um body obrigatíório"""
    if body_request.song.upper() == "PING":
        data_ = f"Pong ! ! !\n para o jogador: {body_request.name}"
        response.status_code = status.HTTP_200_OK
    else:
        data_ = "Invalid Song!"
        response.status_code = status.HTTP_400_BAD_REQUEST
    return DefaulApiResponse(data=data_)


async def route_get(response: Response, word=None) -> DefaulApiResponse:
    """Função para a rota de get do ping pong, com parâmetros não obrigatórios"""
    word_is_str = type(word) is str
    word_is_ping = word.upper() == "PING" or word.upper() == "P1NG"
    data_ = "PONG" if word_is_ping and word_is_str else "Invalid Song!"
    response.status_code = status.HTTP_200_OK
    return DefaulApiResponse(data=data_)


async def route_put(response: Response, body_request: PingPongRequestBody) -> DefaulApiResponse:
    """Função para a rota de put do ping pong, sem parâmetros"""
    data_ = f"{body_request.song.upper()} its your song! ! !"
    response.status_code = status.HTTP_201_CREATED
    return DefaulApiResponse(data=data_)


async def route_delete(response: Response) -> DefaulApiResponse:
    """Função para a rota de delete do ping pong, sem parâmetros, funciona randomicamente"""
    check = (randint(1, 999) % 5) == 0
    data_ = "DELETED........... " if check else "Try again...."
    response.status_code = status.HTTP_200_OK if check else status.HTTP_406_NOT_ACCEPTABLE
    return DefaulApiResponse(data=data_)
