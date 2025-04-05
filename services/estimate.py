from re import I
from typing_extensions import LiteralString
from schemas.response.errors import Error
from schemas.response.estimate import ImportResponse
from schemas.request.estimate import UpdateStatus
from schemas.converter import Converter
from config.dependencies import db
from models.models import Assignment, Estimate_Room, Insured, Estimate, Category, Item, Room
from sqlalchemy.exc import IntegrityError


def insert_estimate(converter: Converter):
    mapped_insured = Insured(
        id = converter.insured.id,
        name = converter.insured.name,
        street = converter.insured.street,
        city = converter.insured.city,
        state = converter.insured.state,
        zip = converter.insured.zip
    )
    db.add(mapped_insured)
    # db.commit()

    try:
        mapped_assignment = Assignment(
            claim_number = converter.assignment.claim_number,
            policy_number = converter.assignment.policy_number,
            loss_date = converter.assignment.loss_date,
            insured_id = converter.assignment.insured_id
        )
        db.add(mapped_assignment)
        db.commit()
    except IntegrityError:
        return Error(status_code=422, message="Assignment already exists")

    mapped_estimate = Estimate(
        id = converter.estimate.id,
        status = converter.estimate.status,
        timestamp = converter.estimate.timestamp
    )
    db.add(mapped_estimate)
    # db.commit()

    try:
        for category in converter.categories:
            mapped_category = Category(
                code = category.code,
                description = category.description,
                subcategory = category.subcategory
            )
            db.add(mapped_category)
            db.commit()
    except IntegrityError:
        return Error(status_code=422, message="Category already exists")

    try:
        for item in converter.items:
            mapped_item = Item(
                code = item.code,
                description = item.description,
                quantity = item.quantity,
                uom = item.uom,
                unit_price = item.unit_price,
                extension = item.extension,
                category_code = item.category_code,
                subcategory_code = item.subcategory_code,
                estimate_id = item.estimate_id
            )
            db.add(mapped_item)
            db.commit()
    except IntegrityError:
        return Error(status_code=422, message="Item already exists")

    for room in converter.rooms:
        mapped_room = Room(
            id = room.id,
            name = room.name,
            length = room.length,
            width = room.width,
            height = room.height
        )
        db.add(mapped_room)
        db.commit()

    for estimate_room in converter.estimate_room:
        mapped_est_room = Estimate_Room(
            estimate_id = estimate_room.estimate_id,
            room_id = estimate_room.room_id
        )
        db.add(mapped_est_room)
        db.commit()

    # Successfully imported, change estimate status to "Submitted"
    update_estimate_status(converter.estimate.id, UpdateStatus(status="Submitted"))

    return ImportResponse(
        success = True,
        estimate_id = converter.estimate.id,
        status = "received",
        timestamp = converter.estimate.timestamp,
        validation_results = None
    )

def get_estimate_by_id(id):
    estimate = db.query(Estimate).filter(Estimate.id == id).first()
    return estimate

def update_estimate_status(id: str, status: UpdateStatus):
    estimate = get_estimate_by_id(id)
    if not estimate:
        return None
    estimate.status = status.status

    db.commit()
    db.refresh(estimate)
    return estimate
