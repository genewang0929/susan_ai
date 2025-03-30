from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Insured(Base):
    __tablename__ = "insured"

    insured_id = Column(String, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
