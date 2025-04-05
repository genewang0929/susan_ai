from pydantic import BaseModel

class Error(BaseModel):
    status_code: int
    message: str
