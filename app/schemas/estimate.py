from typing_extensions import Literal
from pydantic import BaseModel, model_validator
import uuid
import time
from datetime import datetime

class Estimate(BaseModel):
    id: str = "estimate_" + str(uuid.uuid4())
    status: Literal["Draft", "Submitted", "In Review", "Approved", "Rejected", "Completed"] = "Draft"
    timestamp: str = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    @model_validator(mode="before")
    @classmethod
    def check_not_none(cls, values):
        for field, value in values.items():
            if value is None:
                raise ValueError(f"{field} cannot be None")
        return values
