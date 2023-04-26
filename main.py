from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models, schemas, crud
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
def read_user(code: str, db: Session = Depends(get_db)):
    currency_info = crud.get_currency(db, code)
    return currency_info


@app.get("/info/{code}")
def read_user(code: str, db: Session = Depends(get_db)):
    currency_info = crud.get_info(db, code)
    return currency_info
