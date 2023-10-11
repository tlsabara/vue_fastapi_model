import json
import os
from datetime import datetime, timedelta

from fastapi import Response, status, HTTPException

from api.api_core.bases.on_request import AuthRequestBody
from api.api_core.bases.on_response import DefaulApiResponse, ApiResposeAuthToken
from api.api_core.v1.utils import generate_jwt


async def generate_auth_token(body_request: AuthRequestBody) -> ApiResposeAuthToken | DefaulApiResponse:
    """Authentication Route

    Generate authentication tokens for API
    """
    if body_request.access_id != body_request.access_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong credentials")

    jwt_ = generate_jwt()

    return ApiResposeAuthToken(token=jwt_, msg="success")
