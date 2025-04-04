from fastapi import APIRouter
from schemas.request.estimate import UpdateStatus
from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
import xml.etree.ElementTree as ET
from services.reference import get_all_categories, get_all_line_items

router = APIRouter(prefix="/api/reference", tags=["Reference"])

@router.get("/categories")
async def get_categories():
    return get_all_categories()

@router.get("/line-items")
async def get_line_items():
    return get_all_line_items()
