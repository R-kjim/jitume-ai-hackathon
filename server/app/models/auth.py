from pydantic import EmailStr

from server.app.models.base import BaseModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean, Enum

from datetime import datetime
from typing import Optional

import enum


class UserRole(enum.Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    SALES_AGENT = "Sales Agent"
    CLIENT = "Client"



class User(BaseModel):

    __tablename__ = "users"

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    email: Mapped[EmailStr] = mapped_column(
        String,
        nullable=False,
        unique=True,
        index=True
    )

    password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.CLIENT,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    last_login: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        nullable=True
    )