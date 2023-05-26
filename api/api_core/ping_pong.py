from random import randint

from api.api_core.bases.on_request import PingPongRequestBody
from api.api_core.bases.on_response import DefaulApiResponse


async def route_post(body_request: PingPongRequestBody) -> DefaulApiResponse:
    """Função rota de post do ping pong, com parâmetros não obrigatórios, mas com um body obrigatíório
    """
    if body_request.song.upper() == 'PING':
        data_ = f'Pong ! ! !\n para o jogador: {body_request.name}'
    else:
        data_ = 'Invalid Song!'
    return DefaulApiResponse(message=data_).set_method('POST')


async def route_get(word=None) -> DefaulApiResponse:
    """Função para a rota de get do ping pong, com parâmetros não obrigatórios
    """
    word_is_str = type(word) is str
    word_is_ping = word.upper() == 'PING' or word.upper() == 'P1NG'
    data_ = 'PONG' if word_is_ping and word_is_str else 'Invalid Song!'
    return DefaulApiResponse(message=data_).set_method('GET')


async def route_put(body_request: PingPongRequestBody) -> DefaulApiResponse:
    """Função para a rota de put do ping pong, sem parâmetros
    """
    data_ = f'{body_request.song.upper()} its your song! ! !'
    return DefaulApiResponse(message=data_).set_method('PUT')


async def route_delete(body_request: PingPongRequestBody) -> DefaulApiResponse:
    """Função para a rota de delete do ping pong, sem parâmetros
    """
    check = (randint(1, 999) % 5) == 0
    data_ = 'DELETED........... ' if check else 'Try again....'
    return DefaulApiResponse(message=data_).set_method('DELETE')
