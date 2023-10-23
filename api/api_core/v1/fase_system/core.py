import json

from fastapi import HTTPException, status, Response, Path

from api.api_core.v1.fase_system.utils import collect_view_data
from api.api_core.bases.on_response import DefaulApiResponse
from api.api_core.bases.on_response import DefaulApiResponse


async def route_get(response: Response, vw_name: str) -> DefaulApiResponse:
    try:
        data_ = json.loads(collect_view_data(viewname=f"siclo_pnm.{vw_name}").getvalue())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY
        )
    else:
        return DefaulApiResponse(
            data=data_
        )

