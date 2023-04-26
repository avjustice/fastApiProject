from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
import crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Simple Conversion"}


@app.get("/{code}")
def read_code(code: str, db: Session = Depends(get_db)):
    currency_info = crud.get_currency(db, code)
    return currency_info


@app.get("/exchange/{code}")
def read_exchange(code: str, db: Session = Depends(get_db)):
    currency_info = crud.get_exchange_from_code(db, code)
    return currency_info


@app.post("/conversion/")
def convert(source_currency: str, target_currency: str, amount: float, db: Session = Depends(get_db)):
    conversion = crud.convert(amount, source_currency, target_currency, db)
    return conversion
