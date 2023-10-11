from typing import Any

from fastapi import HTTPException, status, logger, Path

from api.api_core.bases.on_response import DefaulApiResponse
from api.api_core.bases.on_request import TwiceRequestBody


async def route_post(body_request: TwiceRequestBody) -> Any:
    """POST Route, to multiply a number
    """
    logger.logger.info(f"request: passou aqui")
    if body_request.number != 0:
        return DefaulApiResponse(
            msg=f"valor {body_request.number*2}"
        )
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="number is 0"
        )


async def route_get(number: int = Path(gt=0)) -> DefaulApiResponse:
    return DefaulApiResponse(
        msg=f"valor: {number*2}"
    )
