from django.shortcuts import render
from django.views import View


class ChatRoomView(View):
    def get(self, request, room_name):
        return render(request, 'chat/chat-room.html', {
            'room_name': room_name
        })
