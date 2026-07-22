from fastapi import APIRouter
from server.app.api import (
    auth, agents
)

router = APIRouter()

router.include_router(
    auth.router, prefix="/auth"
)

router.include_router(
    agents.router, prefix="/agents"
)