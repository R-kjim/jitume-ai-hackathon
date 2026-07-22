from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_async_db
from app.models.user import User, UserRole
from app.schemas.auth import UserLoginPayload
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


# -------------------------
# Login
# -------------------------

@router.post("/login")
async def user_login(
    data: UserLoginPayload,
    db: AsyncSession = Depends(get_async_db),
):
    return {
        "message": "Login endpoint reached",
        "email": data.email,
    }


# -------------------------
# Create User
# -------------------------

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_async_db),
):

    existing = await db.execute(
        select(User).where(User.email == payload.email)
    )

    if existing.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists.",
        )

    user = User(
        name=payload.name,
        email=payload.email,
        password=payload.password,      # TODO: Hash password
        role=payload.role,
    )

    db.add(user)

    await db.commit()
    await db.refresh(user)

    return user


# -------------------------
# Get All Users
# -------------------------

@router.get(
    "/",
    response_model=list[UserResponse],
)
async def get_users(
    db: AsyncSession = Depends(get_async_db),
):

    result = await db.execute(
        select(User)
    )

    return result.scalars().all()


# -------------------------
# Get User
# -------------------------

@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_async_db),
):

    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return user


# -------------------------
# Update User
# -------------------------

@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
async def update_user(
    user_id: UUID,
    payload: UserUpdate,
    db: AsyncSession = Depends(get_async_db),
):

    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)

    return user


# -------------------------
# Delete User
# -------------------------

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_async_db),
):

    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    await db.delete(user)
    await db.commit()

    return {
        "message": "User deleted successfully.",
    }


# -------------------------
# Users By Role
# -------------------------

@router.get(
    "/role/{role}",
    response_model=list[UserResponse],
)
async def get_users_by_role(
    role: UserRole,
    db: AsyncSession = Depends(get_async_db),
):

    result = await db.execute(
        select(User).where(User.role == role)
    )

    return result.scalars().all()


# -------------------------
# User By Email
# -------------------------

@router.get(
    "/email/{email}",
    response_model=UserResponse,
)
async def get_user_by_email(
    email: str,
    db: AsyncSession = Depends(get_async_db),
):

    result = await db.execute(
        select(User).where(User.email == email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return user

