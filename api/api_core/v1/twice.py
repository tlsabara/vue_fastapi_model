from typing import Any

from fastapi import HTTPException, status, logger, Path, Response

from api.api_core.bases.on_response import DefaulApiResponse
from api.api_core.bases.on_request import TwiceRequestBody


async def route_post(response: Response, body_request: TwiceRequestBody) -> Any:
    """POST Route, to multiply a number
    """
    logger.logger.info(f"request: passou aqui")
    if body_request.number != 0:
        response.status_code = status.HTTP_200_OK
        return DefaulApiResponse(
            data=body_request.number*2
        )
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="number is 0"
        )


async def route_get(response: Response, number: int = Path(gt=0)) -> DefaulApiResponse:
    """GET Route, just mutiply a number, with validaiton path
    """
    response.status_code = status.HTTP_200_OK
    return DefaulApiResponse(
        data=number*2
    )
