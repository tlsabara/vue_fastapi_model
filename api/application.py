import logging
import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from pydantic import BaseSettings


from api.orm import models, db
from api.api_core import ping_pong, root
from api.api_core.v1.auth import http_auth as v1_auth
from api.api_core.v1.auth.bearer_control import ApiBearer
from api.api_core.v1 import twice as v1_twice
from api.api_core.v1 import foo as v1_foo

load_dotenv()

__version__ = "0.5.0"
os.environ["APP_VERSION"] = __version__

homolog_or_test = (
        os.environ.get("DEV_ENV") == "True" or os.environ.get("TEST_ENV") == "True"
)


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json" if homolog_or_test else ""

models.OrmBase.metadata.create_all(bind=db.engine)

settings = Settings()
app = FastAPI(
    openapi_url=settings.openapi_url,
)

API_VERSION = "v1"
os.environ["API_VERSION"] = API_VERSION

# Routes to check server status
app.add_api_route("/v1/hello", root.rota_teste, methods=["get"])

# Routes to auhentication
app.add_api_route("/v1/auth", v1_auth.generate_auth_token, methods=["post"])

# Application Routes

## Ping Pong Routes
app.add_api_route("/v1/ping", ping_pong.route_post, methods=["post"], dependencies=[Depends(ApiBearer())])
app.add_api_route("/v1/ping/{word}", ping_pong.route_get, methods=["get"], dependencies=[Depends(ApiBearer())])
app.add_api_route("/v1/ping", ping_pong.route_put, methods=["put"], dependencies=[Depends(ApiBearer())])
app.add_api_route("/v1/ping", ping_pong.route_delete, methods=["delete"], dependencies=[Depends(ApiBearer())])

## Math Routes
app.add_api_route("/v1/calcs/twice", v1_twice.route_post, methods=["post"], dependencies=[Depends(ApiBearer())])
app.add_api_route("/v1/calcs/twice/{number}", v1_twice.route_get, methods=["get"], dependencies=[Depends(ApiBearer())])

app.add_api_route("/v1/foo", v1_foo.route_get, methods=["get"], dependencies=[Depends(ApiBearer())])
