from uuid import UUID

from pydantic import BaseModel, EmailStr

from server.app.models.user import UserRole


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    role: UserRole | None = None


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole

    model_config = {
        "from_attributes": True,
    }
    