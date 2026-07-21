from collections import defaultdict
from typing import Dict, Set
import uuid

from fastapi import WebSocket


class WebSocketManager:
    """
    Handles all websocket connections.

    Supports:
        - Multiple meetings
        - Multiple users per meeting
        - Personal messages
        - Meeting broadcasts
        - Global broadcasts
    """

    def __init__(self):
        # client_id -> websocket
        self.connections: Dict[str, WebSocket] = {}

        # meeting_id -> client_ids
        self.rooms: Dict[str, Set[str]] = defaultdict(set)

    async def connect(
        self,
        websocket: WebSocket,
        meeting_id: str,
    ) -> str:
        """
        Accept a websocket connection and add it to a meeting room.
        """

        await websocket.accept()

        client_id = str(uuid.uuid4())

        self.connections[client_id] = websocket
        self.rooms[meeting_id].add(client_id)

        return client_id

    async def disconnect(
        self,
        client_id: str,
        meeting_id: str,
    ):
        """
        Remove a websocket connection.
        """

        self.connections.pop(client_id, None)

        if meeting_id in self.rooms:
            self.rooms[meeting_id].discard(client_id)

            # Remove room if empty
            if not self.rooms[meeting_id]:
                del self.rooms[meeting_id]

    async def send_personal_message(
        self,
        client_id: str,
        payload: dict,
    ):
        """
        Send a message to one client.
        """

        websocket = self.connections.get(client_id)

        if websocket:
            await websocket.send_json(payload)

    async def broadcast_to_meeting(
        self,
        meeting_id: str,
        payload: dict,
    ):
        """
        Broadcast a message to everyone in a meeting.
        """

        if meeting_id not in self.rooms:
            return

        disconnected = []

        for client_id in self.rooms[meeting_id]:
            websocket = self.connections.get(client_id)

            if websocket:
                try:
                    await websocket.send_json(payload)
                except Exception:
                    disconnected.append(client_id)

        # Clean up broken connections
        for client_id in disconnected:
            self.connections.pop(client_id, None)
            self.rooms[meeting_id].discard(client_id)

    async def broadcast_all(
        self,
        payload: dict,
    ):
        """
        Broadcast to all connected clients.
        """

        disconnected = []

        for client_id, websocket in self.connections.items():
            try:
                await websocket.send_json(payload)
            except Exception:
                disconnected.append(client_id)

        # Remove broken connections
        for client_id in disconnected:
            self.connections.pop(client_id, None)

            for room in self.rooms.values():
                room.discard(client_id)

    async def meeting_size(
        self,
        meeting_id: str,
    ) -> int:
        """
        Return number of clients in a meeting.
        """

        return len(self.rooms.get(meeting_id, set()))

    async def active_connections(self) -> int:
        """
        Return total active websocket connections.
        """

        return len(self.connections)

    async def list_clients(
        self,
        meeting_id: str,
    ) -> list[str]:
        """
        Return all client IDs in a meeting.
        """

        return list(self.rooms.get(meeting_id, set()))


# ======================================================
# Singleton instance used throughout the application
# ======================================================

websocket_manager = WebSocketManager()
