from django.shortcuts import render


def index(request):
    return render(request, "websocket_t/index.html", {})


def room(request, room_name):
    return render(request, "websocket_t/room.html", {"room_name": room_name})
