from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from server.app.models.conversation import (
    SpeakerRole,
    ConversationStatus,
)


class ConversationBase(BaseModel):
    meeting_id: UUID
    sequence_number: int
    speaker: SpeakerRole
    speaker_label: Optional[str] = None
    message: str


class ConversationCreate(ConversationBase):
    pass


class ConversationUpdate(BaseModel):
    speaker_label: Optional[str] = None
    message: Optional[str] = None
    confidence_score: Optional[float] = None
    ai_summary: Optional[str] = None
    ai_entities: Optional[str] = None
    ai_processed: Optional[bool] = None
    status: Optional[ConversationStatus] = None


class ConversationResponse(ConversationBase):
    id: UUID
    confidence_score: Optional[float]
    ai_summary: Optional[str]
    ai_entities: Optional[str]
    ai_processed: bool
    status: ConversationStatus
    timestamp: datetime

    class Config:
        from_attributes = True
        