from django.urls import path
from .views import ChatRoomView

urlpatterns = [
    path('<str:room_name>/', ChatRoomView.as_view(), name='chat-room'),
]
