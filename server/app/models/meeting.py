from datetime import datetime, timezone
from enum import Enum as PyEnum

from sqlalchemy import String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class MeetingPlatform(PyEnum):
    GOOGLE_MEET = "Google Meet"
    ZOOM = "Zoom"
    MICROSOFT_TEAMS = "Microsoft Teams"
    OTHER = "Other"


class MeetingStatus(PyEnum):
    CREATED = "Created"
    RECORDING = "Recording"
    TRANSCRIBED = "Transcribed"
    SUMMARIZED = "Summarized"
    PROPOSAL_GENERATED = "Proposal Generated"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Meeting(BaseModel):
    __tablename__ = "meetings"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    client_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    platform: Mapped[MeetingPlatform] = mapped_column(
        Enum(MeetingPlatform),
        default=MeetingPlatform.GOOGLE_MEET,
        nullable=False,
    )

    meeting_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    meeting_link: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    fathom_meeting_id: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True,
    )

    recording_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    transcript_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    status: Mapped[MeetingStatus] = mapped_column(
        Enum(MeetingStatus),
        default=MeetingStatus.CREATED,
        nullable=False,
    )

    # Relationship with conversations
    conversations: Mapped[list["Conversation"]] = relationship(
        "Conversation",
        back_populates="meeting",
        cascade="all, delete-orphan",
        lazy="selectin",
    )