from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine, get_db
from parsing import get_full_currency_info, get_currency_info
import schedule
import time
import sqlalchemy.exc


def insert(db: Session):
    full_currency_info = get_full_currency_info()
    for code, name, rate in full_currency_info:
        currency = models.Currency(code=code, name=name, rate=rate)
        db.add(currency)
        db.commit()
    print('Inserted')


def update(db: Session = SessionLocal()):
    updated_info = get_currency_info()
    for code, rate in updated_info.items():
        db.query(models.Currency).filter(models.Currency.code == code).update({'rate': rate})
        db.commit()
    print('Updated')


def main():
    models.Base.metadata.create_all(bind=engine)
    try:
        insert(SessionLocal())
    except sqlalchemy.exc.IntegrityError:
        pass
    schedule.every(3).hours.do(update, db=SessionLocal())
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
