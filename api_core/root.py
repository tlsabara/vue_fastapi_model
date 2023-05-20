from fastapi import Response, status


def global_route(response: Response):
    response.status_code = status.HTTP_403_FORBIDDEN
    return {'message': 'invalid_resource'}