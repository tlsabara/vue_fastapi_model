from fastapi import Response, status


def global_route(response: Response):
    """Rota de resposta padrão da aplicação."""
    response.status_code = status.HTTP_403_FORBIDDEN
    return {"message": "invalid_resource", "status": "error", "status_code": 200}
