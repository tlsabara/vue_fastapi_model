import os
from typing import Any
from pydantic import BaseModel
from datetime import datetime

sb_type = list | dict | float | str  # sb sou eu.


class BaseApiResponse(BaseModel):
    time: datetime
    api_version: str
    app_version: str
    method: str = 'unknown method'

    def __init__(self, **data: Any):
        data.update({
            'time': datetime.now(),
            'api_version': os.environ.get('API_VERSION'),
            'app_version': os.environ.get('APP_VERSION'),
        })
        super().__init__(**data)

    def set_method(self, vlr:str):
        self.method = vlr
        return self


class DefaulApiResponse(BaseApiResponse):
    message: sb_type


class ApiResposeAuthToken(BaseApiResponse):
    token: str

