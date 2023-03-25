from . import consumers
from django.urls import path

ws_patterns = [
    path('<str:group_name>/', consumers.ChatConsumer.as_asgi()),
]

