from routes.estimate import router as estimate_router
from routes.reference import router as reference_router
from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import ValidationError

app = FastAPI()

# Include API routes
app.include_router(estimate_router)
app.include_router(reference_router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to My FastAPI App!"}


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    errors = [{"message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"errors": errors})

# @app.post("/estimate/import")
# async def import_estimates(file: UploadFile = File(...)):
#     content = await file.read()

#     converter = Converter()

#     root = ET.fromstring(content)
#     insured = Insured(
#         name = root.findall("./ASSIGNMENT/INSURED/NAME")[0].text,
#         street = root.findall("./ASSIGNMENT/INSURED/ADDRESS/STREET")[0].text,
#         city = root.findall("./ASSIGNMENT/INSURED/ADDRESS/CITY")[0].text,
#         state = root.findall("./ASSIGNMENT/INSURED/ADDRESS/STATE")[0].text,
#         zip = root.findall("./ASSIGNMENT/INSURED/ADDRESS/ZIP")[0].text
#     )
#     print(insured)
#     converter.insured = insured


#     assignment = Assignment(
#         claim_number = root.findall("./ASSIGNMENT/CLAIM_NUMBER")[0].text,
#         policy_number = root.findall("./ASSIGNMENT/POLICY_NUMBER")[0].text,
#         loss_date = root.findall("./ASSIGNMENT/LOSS_DATE")[0].text,
#         insured_id = insured.id
#     )
#     print(assignment)
#     converter.assignment = assignment


#     estimate = Estimate()
#     print(estimate)
#     converter.estimate = estimate


#     line_items = root.findall("./ESTIMATE/LINE_ITEMS/ITEM")
#     for line_item in line_items:
#         quantity = line_item.findall("./QUANTITY")[0].text
#         unit_price = line_item.findall("./UNIT_PRICE")[0].text
#         extension = line_item.findall("./EXTENSION")[0].text
#         category_code_str = line_item.findall("./CATEGORY_CODE")[0].text
#         if quantity is None or unit_price is None or extension is None or category_code_str is None:
#             return JSONResponse(status_code=422, content={"errors": "Quantity, unit price, extension, and category code cannot be None"})

#         category_code = category_code_str.split('-')[0]
#         subcategory_code = category_code_str.split('-')[1]
#         category = Category(code=category_code, subcategory=subcategory_code)
#         converter.categories.append(category)

#         item = Item(
#             code = line_item.findall("./CODE")[0].text,
#             description = line_item.findall("./DESCRIPTION")[0].text,
#             quantity = float(quantity),
#             uom = line_item.findall("./UOM")[0].text,
#             unit_price = float(unit_price),
#             extension = float(extension),
#             category_code = category_code,
#             subcategory_code = subcategory_code,
#             estimate_id = estimate.id
#         )
#         print(item)
#         converter.items.append(item)


#     rooms = root.findall("./ESTIMATE/ROOMS/ROOM")
#     for r in rooms:
#         length = r.findall("./DIMENSIONS/LENGTH")[0].text
#         width = r.findall("./DIMENSIONS/WIDTH")[0].text
#         height = r.findall("./DIMENSIONS/HEIGHT")[0].text
#         if length is None or width is None or height is None:
#             return JSONResponse(status_code=422, content={"errors": "Length, width, and height cannot be None"})

#         room = Room(
#             name = r.findall("./NAME")[0].text,
#             length = float(length),
#             width = float(width),
#             height = float(height)
#         )
#         print(room)
#         converter.rooms.append(room)

#         estimate_room = Estimate_Room(
#             estimate_id = estimate.id,
#             room_id = room.id
#         )
#         print(estimate_room)
#         converter.estimate_room.append(estimate_room)

#     return insert_estimate(converter)

# @app.get("/estimate/{id}")
# async def get_estimate(id: str):
#     return get_estimate_by_id(id)



# @app.get("/reference/categories")
# async def get_categories():
#     return get_all_categories()

# @app.get("/reference/line-items")
# async def get_line_items():
#     return get_all_line_items()

# @app.put("/estimate/{id}/status")
# async def update_status(id: str, status: UpdateStatus):
#     return update_estimate_status(id, status)
