from typing_extensions import Literal
from pydantic import BaseModel
import uuid
import time
from datetime import datetime

class Estimate(BaseModel):
    id: str = "estimate_" + str(uuid.uuid4())
    status: Literal["Draft", "Submitted", "In Review", "Approved", "Rejected", "Completed"] = "Draft"
    timestamp: str = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
