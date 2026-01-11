from fastapi import APIRouter
from app.services.info_service import get_service_info

router = APIRouter()

@router.get("/info")
def service_info():
    return get_service_info()
