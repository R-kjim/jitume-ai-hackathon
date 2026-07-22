from pydantic import EmailStr

from server.app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean
from datetime import datetime
from typing import Optional

class User(BaseModel):
    __tablename__="users"

    email: Mapped[EmailStr] = mapped_column(String, nullable=False, index= True, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)