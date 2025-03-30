# from routes.assignment import router as assignment_router
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
import xml.etree.ElementTree as ET
from schemas.estimate import Estimate
from schemas.assignment import Assignment
from schemas.insured import Insured
from schemas.item import Item
from schemas.room import Room
from pydantic import ValidationError


app = FastAPI()

# Include API routes
# app.include_router(assignment_router, prefix="/api/assignment", tags=["Assignment"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to My FastAPI App!"}


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    errors = [{"message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"errors": errors})

@app.post("/import")
async def import_estimates(file: UploadFile = File(...)):
    content = await file.read()

    root = ET.fromstring(content)
    insured = Insured(
        name = root.findall("./ASSIGNMENT/INSURED/NAME")[0].text,
        street = root.findall("./ASSIGNMENT/INSURED/ADDRESS/STREET")[0].text,
        city = root.findall("./ASSIGNMENT/INSURED/ADDRESS/CITY")[0].text,
        state = root.findall("./ASSIGNMENT/INSURED/ADDRESS/STATE")[0].text,
        zip = root.findall("./ASSIGNMENT/INSURED/ADDRESS/ZIP")[0].text
    )
    print(insured)


    assignment = Assignment(
        claim_number = root.findall("./ASSIGNMENT/CLAIM_NUMBER")[0].text,
        policy_number = root.findall("./ASSIGNMENT/POLICY_NUMBER")[0].text,
        loss_date = root.findall("./ASSIGNMENT/LOSS_DATE")[0].text,
        insured_id = insured.insured_id
    )
    print(assignment)


    estimate = Estimate()
    print(estimate)


    line_items = root.findall("./ESTIMATE/LINE_ITEMS/ITEM")
    for line_item in line_items:
        quantity = line_item.findall("./QUANTITY")[0].text
        unit_price = line_item.findall("./UNIT_PRICE")[0].text
        extension = line_item.findall("./EXTENSION")[0].text
        if quantity is None or unit_price is None or extension is None:
            return JSONResponse(status_code=422, content={"errors": "Quantity, unit price, and extension cannot be None"})

        item = Item(
            code = line_item.findall("./CODE")[0].text,
            description = line_item.findall("./DESCRIPTION")[0].text,
            quantity = float(quantity),
            uom = line_item.findall("./UOM")[0].text,
            unit_price = float(unit_price),
            extension = float(extension),
            category_code = line_item.findall("./CATEGORY_CODE")[0].text
        )
        print(item)


    rooms = root.findall("./ESTIMATE/ROOMS/ROOM")
    for r in rooms:
        length = r.findall("./DIMENSIONS/LENGTH")[0].text
        width = r.findall("./DIMENSIONS/WIDTH")[0].text
        height = r.findall("./DIMENSIONS/HEIGHT")[0].text
        if length is None or width is None or height is None:
            return JSONResponse(status_code=422, content={"errors": "Length, width, and height cannot be None"})

        room = Room(
            name = r.findall("./NAME")[0].text,
            length = float(length),
            width = float(width),
            height = float(height)
        )
        print(room)
