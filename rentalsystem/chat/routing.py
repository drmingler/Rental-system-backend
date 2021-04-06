from django.urls import re_path

from rentalsystem.chat.consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<user_id>\w+)/$", ChatConsumer.as_asgi()),
]
