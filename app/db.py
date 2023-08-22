import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL = "iris://demo:demo@localhost:1972/USER"

engine = create_engine(DATABASE_URL, echo=True, future=True)

Base: DeclarativeMeta = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    engine.connect()


def get_session():
    session = SessionLocal()
    yield session
