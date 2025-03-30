from pydantic import BaseModel, model_validator

class Item(BaseModel):
    code: str
    description: str | None = None
    quantity: float | None = None
    uom: str | None = None
    unit_price: float | None = None
    extension: float | None = None
    category_code: str

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
