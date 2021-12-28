from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def get():
    return {"health": "OK"}
