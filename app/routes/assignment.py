from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..services.assignment import insert_assignment
from fastapi import FastAPI, UploadFile, File, HTTPException

router = APIRouter(prefix="/api/assignment", tags=["Assignment"])


@router.post("/import")
async def import_estimates(file: UploadFile = File(...)):
    content = await file.read()

    await insert_assignment(content.decode("utf-8"))


    resp_json = {
      "success": True,
      "estimate_id": "EST-20250328-001",
      "status": "received",
      "timestamp": "2025-03-28T14:30:05Z",
      "validation_results": {
        "passed": True,
        "warnings": [
          {
            "code": "WRN-101",
            "message": "Unit price differs from standard by more than 10%",
            "line_item_index": 2
          }
        ]
      }
    }
    return {"message": resp_json}
