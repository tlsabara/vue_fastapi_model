from fastapi import Response, status


def global_route(response: Response):
    """Just for commit3"""
    response.status_code = status.HTTP_403_FORBIDDEN
    return {
        "message": "invalid_resource",
        "status": "error",
        "status_code": 200
    }
