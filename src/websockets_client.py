import asyncio
import websockets

async def connect_to_server():
    async with websockets.connect('ws://localhost:8080/echo') as websocket:
        msg = await websocket.recv()
        print("Message recieved: {}".format(msg))

asyncio.get_event_loop().run_until_complete(connect_to_server())
