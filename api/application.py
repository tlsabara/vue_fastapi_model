import logging
import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from pydantic import BaseSettings

from api.api_core import ping_pong, root
from api.api_core.v1.auth import http_auth as v1_auth
from api.api_core.v1.auth.bearer_control import ApiBearer
from api.api_core.v1 import twice as v1_twice

load_dotenv()

__version__ = "0.4.1-beta.1"
os.environ["APP_VERSION"] = __version__

homolog_or_test = (
        os.environ.get("DEV_ENV") == "True" or os.environ.get("TEST_ENV") == "True"
)


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json" if homolog_or_test else ""


settings = Settings()
app = FastAPI(
    openapi_url=settings.openapi_url,
)

API_VERSION = "v1"
os.environ["API_VERSION"] = API_VERSION

app.add_api_route("/v1/hello", root.global_route, methods=["get"], dependencies=[Depends(ApiBearer())])

app.add_api_route("/v1/ping", ping_pong.route_post, methods=["post"])
app.add_api_route("/v1/ping/{word}", ping_pong.route_get, methods=["get"])
app.add_api_route("/v1/ping", ping_pong.route_put, methods=["put"])
app.add_api_route("/v1/ping", ping_pong.route_delete, methods=["delete"])

app.add_api_route("/v1/auth", v1_auth.on_get, methods=["get"], dependencies=[Depends(ApiBearer())])
app.add_api_route("/v1/auth", v1_auth.on_post, methods=["post"])

app.add_api_route("/v1/calcs/twice", v1_twice.route_post, methods=["post"], dependencies=[Depends(ApiBearer())])

if __name__ == "__main__":
    logging.info(f'API on air! vs: {os.environ.get("API_VERSION")}')
    uvicorn.run(
        app="application:app",
        host="127.0.0.1",
        reload=True
    )
