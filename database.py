# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from typing import AsyncGenerator
# from sqlalchemy.orm import sessionmaker
# import asyncio
# from sqlalchemy.orm import declarative_base
# from models import Base
#
# from config import DB_HOST, DB_NAME, DB_PORT, DB_USER
# DB_URL = f'postgresql+asyncpg://{DB_USER}:@{DB_HOST}/{DB_NAME}'
# engine = create_async_engine(DB_URL)
#
#
# # async_session = async_sessionmaker(engine, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_sessionmaker(engine) as session:
#         yield session
#
#
# async def async_main() -> None:
#     engine = create_async_engine(
#         f'postgresql+asyncpg://{DB_USER}:@{DB_HOST}/{DB_NAME}',
#         echo=True,
#     )
#
#     async_session = async_sessionmaker(engine, expire_on_commit=False)
#
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#
# asyncio.run(async_main())
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_NAME, DB_USER

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:@{DB_HOST}/{DB_NAME}'
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# engine = create_engine(DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = async_sessionmaker(engine)

Base = declarative_base()
