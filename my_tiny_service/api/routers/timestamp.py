from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/timestamp")
def get_timestamp():
    """Returns the current timestamp in ISO format"""
    return {"timestamp": datetime.now().isoformat()}