from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estimate_Item(Base):
    __tablename__ = "estimate_item"

    estimate_id = Column(String, ForeignKey("estimate.estimate_id"), primary_key=True, index=True, nullable=False)
    code = Column(String, ForeignKey("item.code"), primary_key=True, index=True, nullable=False)
