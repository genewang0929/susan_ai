from pydantic import BaseModel

class Estimate_Item(BaseModel):
    estimate_id: str
    code: str
