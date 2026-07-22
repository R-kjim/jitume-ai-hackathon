from sqlalchemy import MetaData, DateTime, Boolean, UUID
from uuid import UUID as PyUUID
import uuid
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import datetime, timezone



metadata=MetaData()
Base=declarative_base(metadata=metadata)

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[PyUUID] =  mapped_column(UUID, primary_key=True, unique=True, nullable=False, default=lambda: str(uuid.uuid4()), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), default=lambda:datetime.now(tz=timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), default=lambda:datetime.now(tz=timezone.utc), onupdate=lambda:datetime.now(tz=timezone.utc))
    is_deleted: Mapped[bool] =  mapped_column(Boolean, nullable=False, default= False)