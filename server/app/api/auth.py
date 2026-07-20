from  fastapi import APIRouter, Depends

from server.app.config.session import get_async_db
from server.app.schemas.auth import UserLoginPayload
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.post("/login")
async def user_login(
    data: UserLoginPayload,
    db: AsyncSession = Depends(get_async_db)
):
    try:
        pass
    except Exception as e:
        pass