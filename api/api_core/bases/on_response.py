import os
from typing import Any
from pydantic import BaseModel
from datetime import datetime
from abc import ABC

sb_type = list | dict | float | str  # sb sou eu.


class DefaultMethods(ABC):
    def __init__(self):
        raise NotImplementedError("this class can't be instanced.")

    ACCEPTED_METHODS = ["GET", "PUT", "POST", "DELETE"]


class BaseApiResponse(BaseModel):
    time_at: datetime
    api_version: str
    app_version: str
    method: str = "unknown method"

    def __init__(self, **data: Any):
        data.update(
            {
                "time": datetime.now(),
                "api_version": os.environ.get("API_VERSION"),
                "app_version": os.environ.get("APP_VERSION"),
            }
        )
        super().__init__(**data)

    def set_http_method(self, vlr: str):
        if vlr not in DefaultMethods.ACCEPTED_METHODS:
            raise ValueError("Method Invalid.")
        self.method = vlr
        return self


class DefaulApiResponse(BaseApiResponse):
    message: sb_type


class ApiResposeAuthToken(BaseApiResponse):
    token: str
