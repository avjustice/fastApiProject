from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from parsing import get_full_currency_info, get_currency_info
import schemas
import asyncio


def insert_into_currency(session: Session, currency: models.Currency):
    session.add(currency)
    session.commit()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def main():
    # print(SessionLocal, SessionLocal())
    # currency_info = get_currency_info()
    # print(currency_info)
    full_currency_info = get_full_currency_info()
    print(full_currency_info)
    for code, name, rate in full_currency_info:
        print(code, name, rate)
        currency = models.Currency(code=code, name=name, rate=rate)
        a = get_db()
        insert_into_currency(next(a), currency)


if __name__ == '__main__':
    main()
