from fastapi import APIRouter
from server.app.api import (
    auth
)

router = APIRouter()

router.include_router(
    auth.router, prefix="/auth"
)