from sqlalchemy.orm import Session
import models


def get_currency(db: Session, code: str):
    info = db.query(models.Currency).filter_by(code=code).first()
    if info:
        return info
    return 'Unknown currency code'


def get_exchange_from_code(db: Session, code: str):
    rate = db.query(models.Currency.rate).filter_by(code=code).scalar()
    info = db.query(models.Currency.code, models.Currency.rate).all()
    if rate:
        response = dict()
        for code, usd_rate in info:
            response[code] = round(usd_rate / rate, 5)
        return response
    return 'Unknown currency code'


def convert(amount, source_currency, target_currency, db):
    source_rate = db.query(models.Currency.rate).filter_by(code=source_currency).scalar()
    target_rate = db.query(models.Currency.rate).filter_by(code=target_currency).scalar()
    if source_rate and target_rate:
        result = (amount / source_rate) * target_rate
        return round(result, 5)
    if source_rate:
        return f'Unknown target_currency'
    if target_currency:
        return f'Unknown source_currency'
    return 'Unknown currencies'
