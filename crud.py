from sqlalchemy.orm import Session
import models


def get_currency(db: Session, code: str):
    info = db.query(models.Currency).filter(models.Currency.code == code).first()
    if info:
        return info
    return 'Unknown currency code'


def get_info(db: Session, code: str):
    rate = db.query(models.Currency.rate).filter(models.Currency.code == code).scalar()
    info = db.query(models.Currency.code, models.Currency.rate).all()
    if rate:
        response = dict()
        for code, usd_rate in info:
            response[code] = round(usd_rate / rate, 4)
        return response
    return 'Unknown currency code'
