from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from .models import Chat, Group
from channels.db import database_sync_to_async


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.group_name = name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, 
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept'
        })
       
    def websocket_receive(self, event):
        chat = Chat.objects.create(
            group = Group.objects.filter(name = self.group_name)[0],
            content = event['text']
        )
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
            'type':'chat.message',
            'message': event['text']
            }
        )
        

    def websocket_disconnect(self, event):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()
    
    def chat_message(self, event):
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
    