from pydantic import BaseModel

class Estimate_Room(BaseModel):
    estimate_id: str
    room_id: str
