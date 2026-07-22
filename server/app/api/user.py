from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_async_db
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)
