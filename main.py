from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from mySocket import manager

app = FastAPI()

@app.get("/")
def hello():
    return {
        "Hello", "World"
    }

@app.websocket('/chat/{userId}/{roomId}')
async def websocket_andpoint(websocket: WebSocket, userId: str, roomId: str):
    await manager.connect(websocket, userId, roomId)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send(userId, roomId, data)
            print(data)
    except WebSocketDisconnect as e:
        print(e)
        manager.disconnect(websocket, userId, roomId)
        print(f"Client #{userId} has disconnected")