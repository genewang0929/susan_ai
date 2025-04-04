from pydantic import BaseModel, model_validator

class Category(BaseModel):
    code: str
    description: str = "No description"
    subcategory: str

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
