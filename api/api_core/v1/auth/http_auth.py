import json
import os
from datetime import datetime, timedelta

from fastapi import Response, status, HTTPException

from api.api_core.bases.on_request import AuthRequestBody
from api.api_core.bases.on_response import DefaulApiResponse, ApiResposeAuthToken
from api.api_core.v1.utils import generate_jwt


def on_get() -> DefaulApiResponse:
    """Rota de resposta teste da aplicação."""
    response = Response()
    response.status_code = status.HTTP_200_OK
    data_ = {"body": "use POST dummy!", "status": "ok", "app_code": 200}
    return DefaulApiResponse(data=data_, msg="warning")


async def on_post(body_request: AuthRequestBody) -> ApiResposeAuthToken | DefaulApiResponse:
    """Rota de autenticação

    Gera um token para uso do sistema.
    """
    if body_request.access_id != body_request.access_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong credentials")

    jwt_ = generate_jwt()

    return ApiResposeAuthToken(token=jwt_, msg="success")
