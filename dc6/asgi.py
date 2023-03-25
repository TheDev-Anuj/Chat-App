import os
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import ws_patterns
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dc6.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': URLRouter(
        ws_patterns
    )
})
