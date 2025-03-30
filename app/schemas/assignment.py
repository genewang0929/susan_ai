from pydantic import BaseModel, model_validator

class Assignment(BaseModel):
    claim_number: str
    policy_number: str
    loss_date: str
    insured_id: str

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
