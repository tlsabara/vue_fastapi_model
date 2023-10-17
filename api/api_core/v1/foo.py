from fastapi import Query


async def route_get(number: int = Query(gt=10, lt=100)):
    """A route to return a square of a number
    """
    return {"data": number ** 2}
