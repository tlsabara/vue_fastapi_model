import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseSettings

from api.api_core import ping_pong, root

load_dotenv() # load_dotenv no lugar do decouple.config por conta do desuso
__version__ = "0.1.5"
os.environ["APP_VERSION"] = __version__

homolog_or_test = os.environ.get('DEV_ENV') or os.environ.get('TEST_ENV')


class Settings(BaseSettings):
    openapi_url: str = "/openapi.json" if homolog_or_test else ''


settings = Settings()
app = FastAPI(openapi_url=settings.openapi_url)

API_VERSION = 'v1'
API_MAIN_VERSION = f'/api/{API_VERSION}'
os.environ['API_VERSION'] = API_VERSION

app.add_api_route("/", root.global_route, methods=['get', 'post', 'put', 'delete'])

app.add_api_route(API_MAIN_VERSION + "/ping", ping_pong.route_get, methods=['get'])
app.add_api_route(API_MAIN_VERSION + "/ping", ping_pong.route_post, methods=['post'])
app.add_api_route(API_MAIN_VERSION + "/ping/{word}", ping_pong.route_get, methods=['get'])
# app.add_api_route(API_MAIN_VERSION + "/ping/{word}", ping_pong.route_post, methods=['post'])

if __name__ == "__main__":
    print(f'API on air! vs: {os.environ.get("API_VERSION")}')
    uvicorn.run(app, host="127.0.0.1", )
