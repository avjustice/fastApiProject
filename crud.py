from sqlalchemy.orm import Session
import models
from database import async_session as SessionLocal, engine
from parsing import get_full_currency_info
import schemas
import asyncio


async def insert_into_currency(session: Session, currency: models.Currency):
    async with session.begin():
        session.add(currency)
        await session.commit()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def main():
    print(SessionLocal, SessionLocal())
    full_currency_info = get_full_currency_info()
    for code, name, rate in full_currency_info:
        print(code, name, rate)
        currency = models.Currency(code=code, name=name, rate=rate)
        await insert_into_currency(SessionLocal(), currency)


asyncio.run(main())
