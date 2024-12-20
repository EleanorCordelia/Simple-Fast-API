from fastapi import APIRouter, Depends
from app.auth import get_user

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user
