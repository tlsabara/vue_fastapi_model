import uvicorn
from fastapi import FastAPI
import os
from api_core import ping_pong, root

__version__ = "0.1.3"
os.environ["API_VERSION"] = __version__

app = FastAPI()

app.add_api_route("/", root.global_route, methods=['get', 'post', 'put', 'delete'], tags=[__version__])
app.add_api_route("", root.global_route, methods=['get', 'post', 'put', 'delete'], tags=[__version__])

API_VERSION = '/api/v1'
API_MAIN_VERSION = API_VERSION

app.add_api_route(API_MAIN_VERSION + "/ping", ping_pong.route_get, methods=['get'], tags=[__version__])
app.add_api_route(API_MAIN_VERSION + "/ping", ping_pong.route_post, methods=['post'], tags=[__version__])
app.add_api_route(API_MAIN_VERSION + "/ping/{word}", ping_pong.route_get, methods=['get'])
# app.add_api_route(API_MAIN_VERSION + "/ping/{word}", ping_pong.route_post, methods=['post'])

if __name__ == "__main__":
    print(f'API on air! vs: {os.environ.get("API_VERSION")}')
    uvicorn.run(app, host="127.0.0.1", )
