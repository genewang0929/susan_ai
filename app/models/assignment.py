from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assignment(Base):
    __tablename__ = "assignment"

    claim_number = Column(String, primary_key=True, index=True, nullable=False)
    policy_number = Column(String, nullable=False)
    loss_date = Column(String, index=True, nullable=False)
    insured_id = Column(String, nullable=False, ForeignKey("insured.id"))
