from fastapi import FastAPI
import os

from app.api.health import router as health_router
from app.api.info import router as info_router

app = FastAPI(title="Reusable Backend Service")

app.include_router(health_router)
app.include_router(info_router)
