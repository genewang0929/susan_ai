from typing_extensions import LiteralString
from schemas.converter import Converter
from dependencies import session
from models import Assignment, Estimate_Room, Insured, Estimate, Item, Room

def insert_estimate(converter: Converter):
    mapped_insured = Insured(
        id = converter.insured.id,
        name = converter.insured.name,
        street = converter.insured.street,
        city = converter.insured.city,
        state = converter.insured.state,
        zip = converter.insured.zip
    )
    session.add(mapped_insured)

    mapped_assignment = Assignment(
        claim_number = converter.assignment.claim_number,
        policy_number = converter.assignment.policy_number,
        loss_date = converter.assignment.loss_date,
        insured_id = converter.assignment.insured_id
    )
    session.add(mapped_assignment)

    mapped_estimate = Estimate(
        id = converter.estimate.id,
        status = converter.estimate.status,
        timestamp = converter.estimate.timestamp
    )
    session.add(mapped_estimate)

    for item in converter.items:
        mapped_item = Item(
            code = item.code,
            description = item.description,
            quantity = item.quantity,
            uom = item.uom,
            unit_price = item.unit_price,
            extension = item.extension,
            category_code = item.category_code,
            estimate_id = item.estimate_id
        )
        session.add(mapped_item)

    for room in converter.rooms:
        mapped_room = Room(
            id = room.id,
            name = room.name,
            length = room.length,
            width = room.width,
            height = room.height
        )
        session.add(mapped_room)

    for estimate_room in converter.estimate_room:
        mapped_est_room = Estimate_Room(
            estimate_id = estimate_room.estimate_id,
            room_id = estimate_room.room_id
        )
        session.add(mapped_est_room)

    session.commit()

    return "data has been inserted"
