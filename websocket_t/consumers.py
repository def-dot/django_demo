import datetime
import json
import os

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class InfoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    def get_cpu_info(self):
        # cpu颗数
        cmd = 'grep "physical id" /proc/cpuinfo | sort -u | wc -l'
        p = os.popen(cmd)
        r = p.read()
        return r

    async def receive(self, text_data=None, bytes_data=None):
        cpu = self.get_cpu_info()
        await self.send(cpu)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(f"room_name {self.room_name} channel_name {self.channel_name}")
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        data = {
            'message': f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:{message}"
        }
        self.send(json.dumps(data))
