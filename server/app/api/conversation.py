from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.session import get_async_db
from app.models.conversation import (
    Conversation,
    ConversationStatus,
)
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)


# --------------------------------------------------------
# Create Conversation
# --------------------------------------------------------
@router.post("/")
async def create_conversation(
    payload: ConversationCreate,
    db: AsyncSession = Depends(get_async_db),
):
    conversation = Conversation(**payload.model_dump())

    db.add(conversation)

    await db.commit()
    await db.refresh(conversation)

    return conversation


# --------------------------------------------------------
# Get all conversations
# --------------------------------------------------------
@router.get("/")
async def get_all_conversations(
    db: AsyncSession = Depends(get_async_db),
):
    result = await db.execute(
        select(Conversation).order_by(Conversation.timestamp)
    )

    return result.scalars().all()


# --------------------------------------------------------
# Get conversations for one meeting
# --------------------------------------------------------
@router.get("/meeting/{meeting_id}")
async def get_meeting_conversations(
    meeting_id: UUID,
    db: AsyncSession = Depends(get_async_db),
):
    result = await db.execute(
        select(Conversation)
        .where(Conversation.meeting_id == meeting_id)
        .order_by(Conversation.sequence_number)
    )

    conversations = result.scalars().all()

    if not conversations:
        raise HTTPException(
            status_code=404,
            detail="No conversations found."
        )

    return conversations


# --------------------------------------------------------
# Get one conversation
# --------------------------------------------------------
@router.get("/{conversation_id}")
async def get_conversation(
    conversation_id: UUID,
    db: AsyncSession = Depends(get_async_db),
):
    conversation = await db.get(
        Conversation,
        conversation_id,
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    return conversation


# --------------------------------------------------------
# Update Conversation
# --------------------------------------------------------
@router.patch("/{conversation_id}")
async def update_conversation(
    conversation_id: UUID,
    payload: ConversationUpdate,
    db: AsyncSession = Depends(get_async_db),
):
    conversation = await db.get(
        Conversation,
        conversation_id,
    )

    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    updates = payload.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(conversation, key, value)

    await db.commit()
    await db.refresh(conversation)

    return conversation
