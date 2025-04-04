from pydantic import BaseModel, model_validator

class Estimate_Room(BaseModel):
    estimate_id: str
    room_id: str

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
