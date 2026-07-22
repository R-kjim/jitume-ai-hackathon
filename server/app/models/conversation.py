# conversation.py
# Defines the database model for storing meeting transcript conversations.
# Each record represents one spoken segment in a meeting and tracks AI processing.

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum as PyEnum
from uuid import UUID as PyUUID

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    String,
    Text,
    UUID,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class SpeakerRole(PyEnum):
    ADMIN = "Admin"
    CLIENT = "Client"


class ConversationStatus(PyEnum):
    CAPTURED = "Captured"
    REVIEWED = "Reviewed"
    PROCESSED = "Processed"


class Conversation(BaseModel):
    __tablename__ = "conversations"

    # Meeting this conversation belongs to
    meeting_id: Mapped[PyUUID] = mapped_column(
        UUID,
        ForeignKey("meetings.id"),
        nullable=False,
        index=True,
    )

    # Order of appearance in transcript
    sequence_number: Mapped[int] = mapped_column(
        nullable=False,
        index=True,
    )

    # Speaker type
    speaker: Mapped[SpeakerRole] = mapped_column(
        Enum(SpeakerRole),
        nullable=False,
        index=True,
    )

    # Actual speaker name
    speaker_label: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # Transcript text
    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Confidence score from transcription engine
    confidence_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # AI-generated summary
    ai_summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # AI-extracted entities/requirements
    ai_entities: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # Whether AI has processed this segment
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

    # Time captured
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True,
    )

    # Relationship to Meeting
    meeting: Mapped["Meeting"] = relationship(
        "Meeting",
        back_populates="conversations",
    )