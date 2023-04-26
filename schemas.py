from pydantic import BaseModel, Field


class CurrencyUnknown(BaseModel):
    message: str


class CurrencyInfo(BaseModel):
    code: str = Field(max_length=3, min_length=3)
    name: str = Field(max_length=100)
    rate: float = Field(gt=0)

    class Config:
        orm_mode = True


class CurrencyRequest(BaseModel):
    amount: float = Field(gt=0)
    source_currency: str = Field(max_length=3, min_length=3)
    target_currency: str = Field(max_length=3, min_length=3)


class CurrencyResponse(BaseModel):
    amount: float = Field(gt=0)
