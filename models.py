from enum import unique
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Text, Column, ForeignKeyConstraint
from sqlalchemy import Table
from typing import List



class Base(DeclarativeBase):
    pass

# Association table for many-to-one relationship between Assignment and Insured
class Assignment(Base):
    __tablename__ = "assignment"

    claim_number:Mapped[str] = mapped_column(primary_key=True)
    policy_number:Mapped[str] = mapped_column(nullable=False)
    loss_date:Mapped[str] = mapped_column(nullable=False)
    insured_id:Mapped[str] = mapped_column(ForeignKey("insured.id"), nullable=False)
    insured:Mapped["Insured"] = relationship(back_populates="assignment")

    def __repr__(self):
        return f"Assignment(claim_number={self.claim_number}, policy_number={self.policy_number}, loss_date={self.loss_date})"


class Insured(Base):
    __tablename__ = "insured"
    id:Mapped[str] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    street:Mapped[str] = mapped_column(nullable=False)
    city:Mapped[str] = mapped_column(nullable=False)
    state:Mapped[str] = mapped_column(nullable=False)
    zip:Mapped[str] = mapped_column(nullable=False)
    assignment:Mapped[List["Assignment"]] = relationship(back_populates="insured")

    def __repr__(self):
        return f"Insured(id={self.id}, name={self.name}, street={self.street}, city={self.city}, state={self.state}, zip={self.zip})"


# estimate_room = Table(
#     "estimate_room",
#     Base.metadata,
#     Column("estimate_id", ForeignKey("estimate.id"), primary_key=True),
#     Column("room_id", ForeignKey("room.id"), primary_key=True),
# )

class Estimate_Room(Base):
    __tablename__ = "estimate_room"

    estimate_id:Mapped[str] = mapped_column(ForeignKey("estimate.id"), primary_key=True)
    room_id:Mapped[str] = mapped_column(ForeignKey("room.id"), primary_key=True)
    estimate:Mapped[List["Estimate"]] = relationship(back_populates="estimate_room")
    room:Mapped[List["Room"]] = relationship(back_populates="estimate_room")


class Estimate(Base):
    __tablename__ = "estimate"

    id:Mapped[str] = mapped_column(primary_key=True)
    status:Mapped[str] = mapped_column(nullable=False)
    timestamp:Mapped[str] = mapped_column(nullable=False)
    item:Mapped[List["Item"]] = relationship(back_populates="estimate")
    estimate_room:Mapped[List["Estimate_Room"]] = relationship(back_populates="estimate")

    def __repr__(self):
        return f"Estimate(id={self.id}, status={self.status}, timestamp={self.timestamp})"


# Association table for many-to-many relationship between Estimate and Room
class Room(Base):
    __tablename__ = "room"

    id:Mapped[str] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    length:Mapped[float] = mapped_column(nullable=False)
    width:Mapped[float] = mapped_column(nullable=False)
    height:Mapped[float] = mapped_column(nullable=False)
    estimate_room:Mapped[List["Estimate_Room"]] = relationship(back_populates="room")

    def __repr__(self):
        return f"Room(id={self.id}, name={self.name}, length={self.length}, width={self.width}, height={self.height})"


# Association table for one-to-many relationship between Category and Item
class Category(Base):
    __tablename__ = "category"

    code:Mapped[str] = mapped_column(primary_key=True, unique=True)
    description:Mapped[str] = mapped_column(nullable=False)
    subcategory:Mapped[str] = mapped_column(primary_key=True, unique=True)
    item:Mapped["Item"] = relationship(back_populates="category")

    def __repr__(self):
        return f"Category(code={self.code}, description={self.description}, subcategory={self.subcategory})"


# Association table for one-to-many relationship between Estimate and Item
class Item(Base):
    __tablename__ = "item"

    code:Mapped[str] = mapped_column(primary_key=True)
    description:Mapped[str] = mapped_column(nullable=False)
    quantity:Mapped[float] = mapped_column(nullable=False)
    uom:Mapped[str] = mapped_column(nullable=False)
    unit_price:Mapped[float] = mapped_column(nullable=False)
    extension:Mapped[float] = mapped_column(nullable=False)
    category_code:Mapped[str] = mapped_column(nullable=False)
    subcategory_code:Mapped[str] = mapped_column(nullable=False)
    estimate_id:Mapped[str] = mapped_column(ForeignKey("estimate.id"), nullable=False)
    estimate:Mapped["Estimate"] = relationship(back_populates="item")
    category:Mapped["Category"] = relationship(back_populates="item")
    __table_args__ = (ForeignKeyConstraint([category_code, subcategory_code], [Category.code, Category.subcategory]), {})

    def __repr__(self):
        return f"Item(code={self.code}, description={self.description}, quantity={self.quantity}, uom={self.uom}, unit_price={self.unit_price}, extension={self.extension}, category_code={self.category_code})"
