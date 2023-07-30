from fastapi import Response, status


def global_route(response: Response):
    """Rota de resposta padrão da aplicação."""
    response.status_code = status.HTTP_200_OK
    return {"message": "Hi", "status": "ok", "status_code": 200}
