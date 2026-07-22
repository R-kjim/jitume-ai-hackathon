from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.config.session import get_async_db
from app.models.user import User
from app.schemas.auth import UserLoginPayload

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
async def login(
    data: UserLoginPayload,
    db: AsyncSession = Depends(get_async_db)
):
    result = await db.execute(
        select(User).where(User.email == data.email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # TODO:
    # Verify hashed password using passlib/bcrypt
    # Generate JWT access token

    return {
        "message": "Login successful",
        "user": {
            "id": str(user.id),
            "email": user.email,
            "role": user.role.value,
        }
    }