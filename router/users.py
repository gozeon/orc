from fastapi import APIRouter, Depends
from dependencies import get_current_user

router = APIRouter(prefix="/users", tags=['users'], )


@router.get("/me")
async def me(user=Depends(get_current_user)):
    return user
