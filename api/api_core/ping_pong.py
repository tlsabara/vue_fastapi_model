from ..setup import __version__


async def route_post(word):
    return {"message": "PONG", "method": "POST", 'word': word, "vs": __version__}


async def route_get(word=None):
    dict_1 = {"message": "PONG", "method": "GET", "vs": __version__}
    return dict_1 if not word else {"message": "PONG", "method": "GET", "word": word, "vs": __version__}


async def route_put():
    return {"message": "PONG", "method": "PUT", "vs": __version__}


async def route_delete():
    return {"message": "PONG", "method": "DELETE", "vs": __version__}

