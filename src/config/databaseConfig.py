from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import getenv

_DATABASE_URL = f"postgresql://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('POSTGRES_DB')}"

_engine = create_engine(_DATABASE_URL)
SessionLocal = sessionmaker(bind=_engine)

Base = declarative_base()

def init_db():
    import model

    Base.metadata.create_all(bind=_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()