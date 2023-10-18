from api.orm.db import OrmBase
from sqlalchemy import Column, Integer,Uuid, String, Boolean, DateTime

class User(OrmBase):
    """Model for users of system.
    """
    __tablename__ = 'tb_users'

    id = Column(String, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    valid_email = Column(Boolean, default=False)
    pin  = Column(Integer)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime)

