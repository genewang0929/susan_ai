from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Estimate_Item(Base):
    __tablename__ = "estimate_room"

    estimate_id = Column(String, ForeignKey("estimate.id"), primary_key=True, index=True, nullable=False)
    room_id = Column(String, ForeignKey("room.id"), primary_key=True, index=True, nullable=False)
