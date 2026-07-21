from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict
import json
import asyncio
import uuid

router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"]
)


class ConnectionManager:
    """
    Handles all active websocket connections.
    """

    def __init__(self):
        self.connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket):
        """
        Accept websocket connection.
        """

        await websocket.accept()

        client_id = str(uuid.uuid4())

        self.connections[client_id] = websocket

        return client_id

    def disconnect(self, client_id: str):

        if client_id in self.connections:
            del self.connections[client_id]

    async def send(self, client_id: str, data: dict):

        websocket = self.connections.get(client_id)

        if websocket:

            await websocket.send_json(data)

    async def broadcast(self, data: dict):

        for websocket in self.connections.values():

            await websocket.send_json(data)


manager = ConnectionManager()


@router.websocket("/conversation")
async def websocket_endpoint(websocket: WebSocket):

    client_id = await manager.connect(websocket)

    await manager.send(
        client_id,
        {
            "type": "connected",
            "message": "Connected successfully",
            "client_id": client_id
        }
    )

    try:

        while True:

            message = await websocket.receive_json()

            event = message.get("event")

            payload = message.get("payload")

            ######################################################
            # 1. Meeting Started
            ######################################################

            if event == "meeting_started":

                await manager.send(
                    client_id,
                    {
                        "type": "status",
                        "message": "Meeting created."
                    }
                )

            ######################################################
            # 2. Audio Chunk
            ######################################################

            elif event == "audio_chunk":

                await manager.send(
                    client_id,
                    {
                        "type": "status",
                        "message": "Audio received."
                    }
                )

                """
                TODO

                Send audio chunk to Whisper Service

                transcript = whisper.transcribe(payload)

                """

            ######################################################
            # 3. Transcript
            ######################################################

            elif event == "transcript":

                transcript = payload

                await manager.send(
                    client_id,
                    {
                        "type": "transcript",
                        "text": transcript
                    }
                )

                """
                Save transcript

                conversation_service.save()

                """

            ######################################################
            # 4. AI Summary
            ######################################################

            elif event == "generate_summary":

                await manager.send(
                    client_id,
                    {
                        "type": "processing",
                        "message": "Generating summary..."
                    }
                )

                await asyncio.sleep(2)

                summary = {

                    "summary":
                        "Meeting summary generated."

                }

                await manager.send(
                    client_id,
                    {
                        "type": "summary",
                        "data": summary
                    }
                )

            ######################################################
            # 5. Proposal
            ######################################################

            elif event == "generate_proposal":

                await manager.send(
                    client_id,
                    {
                        "type": "processing",
                        "message": "Generating proposal..."
                    }
                )

                await asyncio.sleep(2)

                proposal = {

                    "title": "Business Proposal",

                    "sections": [
                        "Introduction",
                        "Problem",
                        "Solution",
                        "Budget"
                    ]
                }

                await manager.send(
                    client_id,
                    {
                        "type": "proposal",
                        "data": proposal
                    }
                )

            ######################################################
            # 6. Broadcast
            ######################################################

            elif event == "broadcast":

                await manager.broadcast(

                    {
                        "type": "broadcast",
                        "message": payload
                    }

                )

            ######################################################

            else:

                await manager.send(

                    client_id,

                    {
                        "type": "error",
                        "message": "Unknown event."
                    }

                )

    except WebSocketDisconnect:

        manager.disconnect(client_id)

        print(f"{client_id} disconnected.")