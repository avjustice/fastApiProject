from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


@app.get("/{code}", response_model=schemas.CurrencyInfo | str)
def read_code(code: str, db: Session = Depends(get_db)):
    currency_info = crud.get_currency(db, code)
    return currency_info


@app.get("/exchange/{code}", response_model=dict | str)
def read_exchange(code: str, db: Session = Depends(get_db)):
    currency_info = crud.get_exchange_from_code(db, code)
    return currency_info


@app.post("/conversion/", response_model=float)
def convert(source_currency: str, target_currency: str, amount: float, db: Session = Depends(get_db)):
    conversion = crud.convert(amount, source_currency, target_currency, db)
    return conversion
