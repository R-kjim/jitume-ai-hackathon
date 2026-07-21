from fastapi import APIRouter

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.get("/")
async def get_all_conversations():

    return {
        "message": "All conversations"
    }


@router.get("/{meeting_id}")
async def get_meeting_conversation(meeting_id: int):

    return {
        "meeting_id": meeting_id,
        "message": "Conversation retrieved"
    }


@router.post("/")
async def create_conversation():

    return {
        "message": "Conversation created"
    }


@router.put("/{conversation_id}")
async def update_conversation(conversation_id: int):

    return {
        "conversation_id": conversation_id,
        "message": "Conversation updated"
    }


@router.delete("/{conversation_id}")
async def delete_conversation(conversation_id: int):

    return {
        "conversation_id": conversation_id,
        "message": "Conversation deleted"
    }