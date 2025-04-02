from pydantic import BaseModel, model_validator
import uuid

class Insured(BaseModel):
    id: str = "insured_" + str(uuid.uuid4())
    name: str
    street: str
    city: str
    state: str
    zip: str

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
