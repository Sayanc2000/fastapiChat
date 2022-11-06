from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        # dictionary of websockets
        self.connections = {}

    async def connect(self, websocket: WebSocket, userId: str, roomId: str):

        await websocket.accept()
        identity = f"{userId}_{roomId}"
        self.connections[identity] = websocket

    def disconnect(self, websocket: WebSocket, userId: str, roomId: str):
        identity = f"{userId}_{roomId}"
        try:
            del self.connections[identity]
        except Exception as e:
            print("already removed websocket")
        # self.connections.remove(websocket)

    async def send(self, userId: str, roomId: str, data):
        identity = f"{userId}_{roomId}"
        for identity in self.connections:
            ids = identity.split("_")
            if ids[1] == roomId:
                await self.connections[identity].send_text(data)

    async def broadcast(self, data):
        for connection in self.connections:
            await connection.send_text(data)


manager = ConnectionManager()