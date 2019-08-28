#!/usr/bin/python
import asyncio
import websockets
import json

import scripts.HandleData as HandD


class WebSocket:

    def __init__(self):
        self.client = {}
        self.start_server()

    async def handle_msg(self, wss, path):
        while True:
            print(wss)
            name = await wss.recv()
            print(name)
            # name = str(name,'utf-8')m
            json_obj = json.loads(name)
            data = HandD.HandleData.handle_data(json_obj)
            print(data)
            if data[2]:
                msg_id = data[1]["msg_id"]
                if msg_id == "loginAck":
                    self.client_connect(data[2], wss)
            await wss.send(json.dumps(data[1]))

    def start_server(self):
        ws = websockets.serve(self.handle_msg, "localhost", 8888)
        asyncio.get_event_loop().run_until_complete(ws)
        asyncio.get_event_loop().run_forever()

    def client_connect(self, data, ws):
        self.client[data["username"]] = ws
        print(self.client)


if __name__ == '__main__':
    web = WebSocket()

