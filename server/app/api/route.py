
from fastapi import APIRouter

from server.app.api import (
    auth,
    conversation,
    websocket
)

router = APIRouter()

router.include_router(auth.router)
router.include_router(websocket.router)

router.include_router(conversation.router)



