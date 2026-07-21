from datetime import datetime, timezone
from enum import Enum as PyEnum
from uuid import UUID as PyUUID

from sqlalchemy import (
    String,
    DateTime,
    Enum,
    Text,
    Boolean,
    Float,
    ForeignKey,
    UUID,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.app.models.base import BaseModel


class SpeakerRole(PyEnum):
    ADMIN = "Admin"
    CLIENT = "Client"


class ConversationStatus(PyEnum):
    CAPTURED = "Captured"
    REVIEWED = "Reviewed"
    PROCESSED = "Processed"


class Conversation(BaseModel):
    __tablename__ = "conversations"


    # Link transcript segment to meeting
    meeting_id: Mapped[PyUUID] = mapped_column(
        UUID,
        ForeignKey("meetings.id"),
        nullable=False,
        index=True,
    )


    # Order of speech in transcript
    sequence_number: Mapped[int] = mapped_column(
        nullable=False,
        index=True,
    )


    # Speaker category
    speaker: Mapped[SpeakerRole] = mapped_column(
        Enum(SpeakerRole),
        nullable=False,
        index=True,
    )


    # Actual speaker name from Fathom/Whisper diarization
    speaker_label: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    # Transcript text
    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )


    # Confidence returned by transcription engine
    confidence_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )


    # AI-generated insights from this conversation segment
    ai_summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


    # Extracted requirements/entities
    ai_entities: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


    # Indicates GPT/AI agent has processed this segment
    ai_processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )


    status: Mapped[ConversationStatus] = mapped_column(
        Enum(ConversationStatus),
        default=ConversationStatus.CAPTURED,
        nullable=False,
        index=True,
    )


    # When this sentence was captured
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True,
    )


    # Optional relationship back to meeting
    meeting = relationship(
        "Meeting",
        back_populates="conversations"
    )
    