from collections import defaultdict
from fastapi import WebSocket
from typing import Dict, Set
import uuid


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

        self.connections.pop(client_id, None)

        if meeting_id in self.rooms:

            self.rooms[meeting_id].discard(client_id)

            if len(self.rooms[meeting_id]) == 0:

                del self.rooms[meeting_id]

    async def send_personal_message(
        self,
        client_id: str,
        payload: dict,
    ):

        websocket = self.connections.get(client_id)

        if websocket:

            await websocket.send_json(payload)

    async def broadcast_to_meeting(
        self,
        meeting_id: str,
        payload: dict,
    ):

        if meeting_id not in self.rooms:

            return

        for client_id in self.rooms[meeting_id]:

            websocket = self.connections.get(client_id)

            if websocket:

                await websocket.send_json(payload)

    async def broadcast_all(
        self,
        payload: dict,
    ):

        for websocket in self.connections.values():

            await websocket.send_json(payload)

    async def meeting_size(
        self,
        meeting_id: str,
    ) -> int:

        return len(self.rooms.get(meeting_id, []))

    async def active_connections(self) -> int:

        return len(self.connections)

    async def list_clients(
        self,
        meeting_id: str,
    ):

        return list(self.rooms.get(meeting_id, []))
    
    