from server.app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, JSON
from typing import Optional, Dict

class Chat(BaseModel):
    __tablename__="chats"

    name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    client: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_message:Mapped[str] = mapped_column(String, nullable=False)
    messages:  Mapped[Dict[str,any]] = mapped_column(JSON, nullable=False)
    proposal: Mapped[Optional[Dict[str,any]]] = mapped_column(JSON, nullable=True)
    quotation:  Mapped[Optional[Dict[str,any]]] = mapped_column(JSON, nullable=True)

