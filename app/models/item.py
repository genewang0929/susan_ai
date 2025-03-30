from sqlalchemy import Column, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "item"

    code = Column(String, primary_key=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Float, index=True, nullable=False)
    uom = Column(String, nullable=True)
    unit_price = Column(Float, nullable=False)
    extension = Column(Float, nullable=True)
    category_code = Column(String, nullable=True)
