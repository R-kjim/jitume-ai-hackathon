from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.app.config.session import get_async_db
from server.app.models.meeting import Meeting
from server.app.schemas.meeting import (
    MeetingCreate,
    MeetingUpdate,
)

router = APIRouter(
    prefix="/meetings",
    tags=["Meetings"],
)


# ---------------------------------------------------------
# Create Meeting
# ---------------------------------------------------------
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_meeting(
    payload: MeetingCreate,
    db: AsyncSession = Depends(get_async_db),
):
    meeting = Meeting(**payload.model_dump())

    db.add(meeting)

    await db.commit()
    await db.refresh(meeting)

    return meeting


# ---------------------------------------------------------
# Get All Meetings
# ---------------------------------------------------------
@router.get("/")
async def get_all_meetings(
    db: AsyncSession = Depends(get_async_db),
):
    result = await db.execute(
        select(Meeting)
        .order_by(Meeting.meeting_date.desc())
    )

    return result.scalars().all()


# ---------------------------------------------------------
# Get One Meeting
# ---------------------------------------------------------
@router.get("/{meeting_id}")
async def get_meeting(
    meeting_id: UUID,
    db: AsyncSession = Depends(get_async_db),
):
    meeting = await db.get(
        Meeting,
        meeting_id,
    )

    if meeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meeting not found.",
        )

    return meeting


# ---------------------------------------------------------
# Update Meeting
# ---------------------------------------------------------
@router.patch("/{meeting_id}")
async def update_meeting(
    meeting_id: UUID,
    payload: MeetingUpdate,
    db: AsyncSession = Depends(get_async_db),
):
    meeting = await db.get(
        Meeting,
        meeting_id,
    )

    if meeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meeting not found.",
        )

    updates = payload.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(meeting, key, value)

    await db.commit()
    await db.refresh(meeting)

    return meeting