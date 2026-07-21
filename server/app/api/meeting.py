from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from server.app.crud.meeting import meeting_crud
from server.app.database.database import get_db
from server.app.schemas.meeting import (
    MeetingCreate,
    MeetingUpdate,
)

router = APIRouter(
    prefix="/meetings",
    tags=["Meetings"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_meeting(
    meeting: MeetingCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new meeting."""

    return await meeting_crud.create(
        db=db,
        meeting=meeting,
    )


@router.get("/")
async def get_meetings(
    db: AsyncSession = Depends(get_db),
):
    """Get all meetings."""

    return await meeting_crud.get_all(db)


@router.get("/{meeting_id}")
async def get_meeting(
    meeting_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    """Get a meeting by ID."""

    meeting = await meeting_crud.get_by_id(
        db,
        meeting_id,
    )

    if meeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meeting not found.",
        )

    return meeting


@router.put("/{meeting_id}")
async def update_meeting(
    meeting_id: UUID,
    meeting_update: MeetingUpdate,
    db: AsyncSession = Depends(get_db),
):
    """Update meeting details."""

    meeting = await meeting_crud.get_by_id(
        db,
        meeting_id,
    )

    if meeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meeting not found.",
        )

    return await meeting_crud.update(
        db=db,
        meeting=meeting,
        update=meeting_update,
    )


@router.delete("/{meeting_id}")
async def delete_meeting(
    meeting_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    """Delete a meeting."""

    meeting = await meeting_crud.get_by_id(
        db,
        meeting_id,
    )

    if meeting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Meeting not found.",
        )

    await meeting_crud.delete(
        db=db,
        meeting=meeting,
    )

    return {
        "message": "Meeting deleted successfully."
    }
