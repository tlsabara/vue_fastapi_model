from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

sql_parameters = {
    'check_same_thread': False
}

db_url = os.environ.get('DATABASE_URL')


engine = create_engine(db_url, connect_args=sql_parameters)


OrmSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

OrmBase = declarative_base()

def connect():
    db = OrmSession()
    try:
        yield db
    finally:
        db.close()
