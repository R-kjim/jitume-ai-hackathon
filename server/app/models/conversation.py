from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    String,
    DateTime,
    Integer,
    Enum,
    Text,
    Boolean,
    Float,
    ForeignKey
)
from datetime import datetime
from enum import Enum as PyEnum

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


    # Meeting this message belongs to
    meeting_id: Mapped[int] = mapped_column(
        ForeignKey("meetings.id"),
        nullable=False,
        index=True
    )


    # Person speaking
    speaker: Mapped[SpeakerRole] = mapped_column(
        Enum(SpeakerRole),
        nullable=False
    )


    # Speech converted to text
    message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )


    # Optional speaker label from transcription service
    speaker_label: Mapped[str] = mapped_column(
        String,
        nullable=True
    )


    # Speech confidence
    confidence_score: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )


    # Has AI already analyzed this message?
    ai_processed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )


    # Conversation processing status
    status: Mapped[ConversationStatus] = mapped_column(
        Enum(ConversationStatus),
        default=ConversationStatus.CAPTURED
    )


    # When message occurred
    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )