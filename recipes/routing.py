from django.urls import re_path
from recipes.consumers import TextRoomConsumer

websocket_urlpatterns = [
    re_path(r"ws/(?P<room_name>\w+)/$", TextRoomConsumer.as_asgi()),
]