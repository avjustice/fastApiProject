from sqlalchemy import Column, String, Float
from database import Base


class Currency(Base):
    __tablename__ = "currency"
    code = Column(String(3), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    rate = Column(Float, nullable=False)
