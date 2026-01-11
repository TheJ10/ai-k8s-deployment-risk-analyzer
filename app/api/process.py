from fastapi import APIRouter
from pydantic import BaseModel
from app.services.process_service import process_input

router = APIRouter()

class ProcessRequest(BaseModel):
	text: str

@router.post("/api/process")
def process(request: ProcessRequest):
	return process_input(request.text)
