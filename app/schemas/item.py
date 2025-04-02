from pydantic import BaseModel, model_validator

class Item(BaseModel):
    code: str
    description: str
    quantity: float
    uom: str
    unit_price: float
    extension: float
    category_code: str
    estimate_id: str

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
