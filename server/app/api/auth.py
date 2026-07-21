from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.app.config.session import get_async_db
from server.app.schemas.auth import UserLoginPayload

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def user_login(
    data: UserLoginPayload,
    db: AsyncSession = Depends(get_async_db),
):
    return {
        "message": "Login endpoint reached",
        "email": data.email,
    }