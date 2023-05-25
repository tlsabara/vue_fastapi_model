from api.api_core.bases.on_request import PingPongRequestBody
from api.api_core.bases.on_response import DefaulApiResponse


async def route_post(body_request: PingPongRequestBody) -> DefaulApiResponse:
    """Função rota de post do ping pong, com parâmetros não obrigatórios, mas com um body obrigatíório
    """
    if body_request.song.upper() == 'PING':
        data_ = f'Pong ! ! !\n para o jogador: {body_request.name}'
    else:
        data_ = 'Invalid Song!'
    return DefaulApiResponse(message=data_)


async def route_get(word=None) -> DefaulApiResponse:
    """Função para a rota de get do ping pong, com parâmetros não obrigatórios
    """
    data_ = 'PONG'
    return DefaulApiResponse(message=data_).set_method('GET')


async def route_put() -> DefaulApiResponse:
    """Função para a rota de put do ping pong, sem parâmetros
    """
    data_ = 'PONG'
    return DefaulApiResponse(message=data_).set_method('PUT')


async def route_delete() -> DefaulApiResponse:
    """Função para a rota de delete do ping pong, sem parâmetros
    """
    data_ = 'PONG'
    return DefaulApiResponse(message=data_).set_method('DELETE')
