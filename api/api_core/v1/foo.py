from typing import Annotated

from fastapi import Query, Response, status, Depends
from sqlalchemy.orm import Session

from api.orm.models import User
from api.orm import db

async def route_get(response: Response, db_: Annotated[Session, Depends(db.connect)], number: int = Query(gt=10, lt=100)):
    """A route to return a square of a number
    """
    response.status_code = status.HTTP_200_OK
    return {"data": db_.query(User).all()}
