from django.urls import path

from websocket_t.consumers import EchoConsumer


websocket_urlpatterns = [
    path('ws/chat', EchoConsumer)
]
