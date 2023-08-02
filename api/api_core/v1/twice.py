from fastapi import HTTPException, status

from api_core.bases.on_response import DefaulApiResponse
from api_core.bases.on_request import TwiceRequestBody


async def route_post(body_request: TwiceRequestBody) -> DefaulApiResponse:
    """Função rota de post, para multiplicar um numero por 2"""
    if body_request.number != 0:
        return DefaulApiResponse(msg=f"valor {body_request.number*2}")
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="number is 0")
