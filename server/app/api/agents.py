from fastapi import APIRouter, Depends, HTTPException, Request

from server.app.config.session import get_async_db
from server.app.schemas.chat import N8nResponse, UserQuery
from server.app.schemas.fathom import FathomMeetingWebhook
from sqlalchemy.ext.asyncio import AsyncSession
from server.app.services.n8n import n8n

router = APIRouter()

@router.post("/fathom-webhook")
async def fathom_webhook(data:FathomMeetingWebhook):
    try:
        print(data)
        return {"res": True}
    except Exception as e:
        print(e)
        raise Exception(str(e))
    
@router.post("/user-chat")
async def user_chat(
    data: UserQuery,
    db: AsyncSession = Depends(get_async_db)
):
    try:
        res = await n8n.chat_with_agent(payload=data)
        return res
    except Exception as e:
        print(e)
        raise HTTPException(
            detail= str(e),
            status_code= 500
        )
    

@router.post("/n8n-hook")
async def n8n_webhook(req:Request):
    data = await req.json()
    print(data)
    return {
        "detail": "Success"
    }