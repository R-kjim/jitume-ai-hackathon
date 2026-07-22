from fastapi import HTTPException

import httpx

from server.app.config.config import variables
from server.app.schemas.chat import UserQuery

class N8nHandler():
    def __init__(self):
        self.N8N_WEBHOOK_URL = variables.n8n_url

    async def chat_with_agent(self, payload: UserQuery):
        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                # Forward the payload data to the n8n webhook
                response = await client.post(
                    self.N8N_WEBHOOK_URL,
                    json={
                        "sessionId": payload.session_id,
                        "chatInput": payload.message
                    }
                )
                response.raise_for_status()
                return response.json()
                
            except httpx.HTTPStatusError as exc:
                raise HTTPException(
                    status_code=exc.response.status_code, 
                    detail=f"n8n error: {exc.response.text}"
                )
            except httpx.RequestError:
                raise HTTPException(
                    status_code=500, 
                    detail="Failed to communicate with the n8n AI workflow."
                )
            
n8n = N8nHandler()