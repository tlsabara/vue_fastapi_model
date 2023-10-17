from fastapi import Response, status


def rota_teste(response: Response):
    """Rota de resposta padrão da aplicação."""
    response.status_code = status.HTTP_200_OK
    return {"message": "Hi", "status": "server on", "status_code": 200}
