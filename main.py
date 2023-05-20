from datetime import datetime

import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException, status

from api_core import ping_pong, root

app = FastAPI()

app.add_api_route("/", root.global_route, methods=['get', 'post'])

API_VERSION = '/api/v1'
API_MAIN_VERSION = API_VERSION

app.add_api_route(API_MAIN_VERSION + "/ping", ping_pong.route_get, methods=['get'])
# app.add_api_route(API_MAIN_VERSION + "/ping/{word}", ping_pong.route_get, methods=['get'])
app.add_api_route(API_MAIN_VERSION + "/ping/{word}", ping_pong.route_post, methods=['post'])




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
