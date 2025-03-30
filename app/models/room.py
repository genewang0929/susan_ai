from sqlalchemy import Column, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Room(Base):
    __tablename__ = "room"

    id = Column(String, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    length = Column(Float, nullable=True)
    width = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
