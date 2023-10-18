from fastapi import Query, Response, status


async def route_get(response: Response, number: int = Query(gt=10, lt=100)):
    """A route to return a square of a number
    """
    response.status_code = status.HTTP_200_OK
    return {"data": number ** 2}
