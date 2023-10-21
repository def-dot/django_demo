from django.urls import re_path

from websocket_t.consumers import ChatConsumer, InfoConsumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    re_path(r'ws/echo/$', InfoConsumer.as_asgi()),
]
