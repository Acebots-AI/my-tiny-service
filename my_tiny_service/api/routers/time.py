from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/timestamp")
def get_current_timestamp():
    return {"timestamp": datetime.utcnow().isoformat()}
