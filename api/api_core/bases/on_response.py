import os
from typing import Any
from pydantic import BaseModel
from datetime import datetime
from abc import ABC

sb_type = list | dict | float | str  # sb sou eu.


class BaseApiResponse(BaseModel):
    """This a class base for all requests bodies
    """
    time_at: datetime
    api_version: str
    app_version: str
    data: sb_type

    def __init__(self, **kwargs: any):
        msg_ = kwargs.get("msg", "")
        data_ = kwargs.get("data", "")

        kwargs.update(
            {
                "time_at": datetime.now(),
                "api_version": os.environ.get("API_VERSION"),
                "app_version": os.environ.get("APP_VERSION"),
                "msg": msg_,
                "data": data_
            }
        )
        super().__init__(**kwargs)


class DefaulApiResponse(BaseApiResponse):
    """Its a basic api response

    All response in this system shold be like this
    """
    msg: sb_type


class ApiResposeAuthToken(DefaulApiResponse):
    """Body for response having a authentication token on body
    """
    token: str


