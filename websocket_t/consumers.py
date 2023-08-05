from channels.generic.websocket import SyncConsumer
from django.contrib.auth.models import User


class EchoConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print(f"self.scope {self.scope}")
        user = self.scope['user']
        path = self.scope['path']

        user_obj = User.objects.filter(username=user)
        self.send({
            'type': 'websocket.send',
            'text': event['text']
        })


class MessagesConsumer:
    pass
