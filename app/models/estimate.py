from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estimate(Base):
    __tablename__ = "estimate"

    id = Column(String, primary_key=True, index=True, nullable=False)
    status = Column(String, index=True, nullable=False)
