import os
from typing import Any
from pydantic import BaseModel
from datetime import datetime
from abc import ABC

sb_type = list | dict | float | str  # sb sou eu.


class BaseApiResponse(BaseModel):
    """This a class base for all requests bodies
    """
    metadata: dict
    data: sb_type


class DefaulApiResponse(BaseApiResponse):
    """Its a basic api response

    All response in this system shold be like this
    """

    def __init__(self, **kwargs):
        print(kwargs)
        print('OI')
        msg_ = kwargs.get("msg", "undefined")
        data_ = kwargs.get("data", "")

        kwargs = {
            "metadata": {
                "time_at": datetime.now(),
                "core_version": os.environ.get("APP_VERSION"),
                "msg": msg_,
            },
            "data": data_
        }

        super().__init__(**kwargs)

class ApiResposeAuthToken(DefaulApiResponse):
    """Body for response having a authentication token on body
    """
    token: str
