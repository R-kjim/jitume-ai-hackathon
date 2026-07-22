from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.meeting import (
    MeetingPlatform,
    MeetingStatus,
)


class MeetingBase(BaseModel):
    title: str
    client_name: str
    platform: MeetingPlatform = MeetingPlatform.GOOGLE_MEET
    meeting_link: Optional[str] = None


class MeetingCreate(MeetingBase):
    pass


class MeetingUpdate(BaseModel):
    title: Optional[str] = None
    client_name: Optional[str] = None
    platform: Optional[MeetingPlatform] = None
    meeting_link: Optional[str] = None
    recording_url: Optional[str] = None
    transcript_url: Optional[str] = None
    fathom_meeting_id: Optional[str] = None
    status: Optional[MeetingStatus] = None


class MeetingResponse(MeetingBase):
    id: UUID
    meeting_date: datetime
    recording_url: Optional[str]
    transcript_url: Optional[str]
    fathom_meeting_id: Optional[str]
    status: MeetingStatus

    class Config:
        from_attributes = True