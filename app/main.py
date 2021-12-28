from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.recordings import router as audio_router

app = FastAPI()

app.include_router(health_router)
app.include_router(audio_router)