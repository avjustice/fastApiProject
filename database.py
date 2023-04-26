from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_NAME, DB_USER

DATABASE_URL = f'postgresql://{DB_USER}:@{DB_HOST}/{DB_NAME}'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# engine = create_async_engine(DATABASE_URL)
# async_session = async_sessionmaker(engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
