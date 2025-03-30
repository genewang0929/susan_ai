from pydantic import BaseModel, model_validator
import uuid

class Room(BaseModel):
    id: str = "room_" + str(uuid.uuid4())
    name: str
    length: float | None = None
    width: float | None = None
    height: float | None = None

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
