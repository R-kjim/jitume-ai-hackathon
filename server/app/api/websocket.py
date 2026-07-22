from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

from server.app.services.websocket_manager import websocket_manager


router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"],
)


@router.websocket("/meetings/{meeting_id}")
async def meeting_websocket(
    websocket: WebSocket,
    meeting_id: str,
):
    """
    WebSocket endpoint for a single meeting.

    Flow

    User
        ↓
    WebSocket
        ↓
    Meeting Room
        ↓
    Transcript
        ↓
    AI Summary
        ↓
    Proposal
    """

    client_id = await websocket_manager.connect(
        websocket,
        meeting_id,
    )

    await websocket_manager.send_personal_message(
        client_id,
        {
            "type": "connected",
            "client_id": client_id,
            "meeting_id": meeting_id,
            "message": "Connected successfully.",
        },
    )

    await websocket_manager.broadcast_to_meeting(
        meeting_id,
        {
            "type": "user_joined",
            "client_id": client_id,
        },
    )

    try:

        while True:

            message = await websocket.receive_json()

            event = message.get("event")
            payload = message.get("payload")

            ##################################################
            # Meeting Started
            ##################################################

            if event == "meeting_started":

                await websocket_manager.broadcast_to_meeting(
                    meeting_id,
                    {
                        "type": "meeting_started",
                        "meeting_id": meeting_id,
                    },
                )

            ##################################################
            # Audio Chunk
            ##################################################

            elif event == "audio_chunk":

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "processing",
                        "message": "Audio received.",
                    },
                )

                """
                TODO

                transcript = whisper_service.transcribe(payload)

                await websocket_manager.broadcast_to_meeting(
                    meeting_id,
                    {
                        "type": "transcript",
                        "text": transcript
                    }
                )
                """

            ##################################################
            # Transcript
            ##################################################

            elif event == "transcript":

                transcript = payload

                """
                TODO

                Save Conversation

                conversation_service.create(
                    meeting_id=meeting_id,
                    transcript=transcript
                )
                """

                await websocket_manager.broadcast_to_meeting(
                    meeting_id,
                    {
                        "type": "transcript",
                        "text": transcript,
                    },
                )

            ##################################################
            # Generate Summary
            ##################################################

            elif event == "generate_summary":

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "processing",
                        "message": "Generating summary...",
                    },
                )

                """
                TODO

                summary = ai_service.generate_summary(
                    meeting_id
                )
                """

                await asyncio.sleep(2)

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "summary",
                        "data": {
                            "summary": "Meeting summary generated.",
                        },
                    },
                )

            ##################################################
            # Generate Proposal
            ##################################################

            elif event == "generate_proposal":

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "processing",
                        "message": "Generating proposal...",
                    },
                )

                """
                TODO

                proposal = proposal_service.generate(
                    meeting_id
                )
                """

                await asyncio.sleep(2)

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "proposal",
                        "data": {
                            "title": "Business Proposal",
                            "sections": [
                                "Introduction",
                                "Problem",
                                "Solution",
                                "Budget",
                            ],
                        },
                    },
                )

            ##################################################
            # Meeting Broadcast
            ##################################################

            elif event == "broadcast":

                await websocket_manager.broadcast_to_meeting(
                    meeting_id,
                    {
                        "type": "broadcast",
                        "message": payload,
                    },
                )

            ##################################################
            # Meeting Statistics
            ##################################################

            elif event == "meeting_info":

                participants = await websocket_manager.meeting_size(
                    meeting_id
                )

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "meeting_info",
                        "participants": participants,
                    },
                )

            ##################################################

            else:

                await websocket_manager.send_personal_message(
                    client_id,
                    {
                        "type": "error",
                        "message": "Unknown event.",
                    },
                )

    except WebSocketDisconnect:

        await websocket_manager.disconnect(
            client_id,
            meeting_id,
        )

        await websocket_manager.broadcast_to_meeting(
            meeting_id,
            {
                "type": "user_left",
                "client_id": client_id,
            },
        )
        