from datetime import datetime
from pydantic import BaseModel, EmailStr


class Speaker(BaseModel):
    display_name: str
    matched_calendar_invitee_email: EmailStr


class TranscriptEntry(BaseModel):
    speaker: Speaker
    text: str
    timestamp: str


class DefaultSummary(BaseModel):
    template_name: str
    markdown_formatted: str


class Assignee(BaseModel):
    name: str
    email: EmailStr
    team: str


class ActionItem(BaseModel):
    description: str
    user_generated: bool
    completed: bool
    recording_timestamp: str
    recording_playback_url: str
    assignee: Assignee


class CalendarInvitee(BaseModel):
    name: str
    matched_speaker_display_name: str
    email: EmailStr
    is_external: bool
    email_domain: str


class RecordedBy(BaseModel):
    name: str
    email: EmailStr
    team: str
    email_domain: str


class CRMContact(BaseModel):
    name: str
    email: EmailStr
    record_url: str


class CRMCompany(BaseModel):
    name: str
    record_url: str


class CRMDeal(BaseModel):
    name: str
    amount: float
    record_url: str


class CRMMatches(BaseModel):
    contacts: list[CRMContact]
    companies: list[CRMCompany]
    deals: list[CRMDeal]


class FathomMeetingWebhook(BaseModel):
    title: str
    meeting_title: str
    meeting_type: str

    url: str
    meeting_url: str
    share_url: str

    created_at: datetime
    scheduled_start_time: datetime
    scheduled_end_time: datetime
    recording_start_time: datetime
    recording_end_time: datetime

    calendar_invitees_domains_type: str
    shared_with: str

    transcript: list[TranscriptEntry]

    default_summary: DefaultSummary

    action_items: list[ActionItem]

    calendar_invitees: list[CalendarInvitee]

    recorded_by: RecordedBy

    crm_matches: CRMMatches