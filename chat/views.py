from django.shortcuts import render
from .models import Group,   Chat
# Create your views here.

def chat(request, group_name):
    group = Group.objects.filter(name = group_name).first()
    if group:
        chats = Chat.objects.filter(group = group)
    else:
        group = Group(name = group_name)
        group.save()
        chats = []
    return render(
        request, 
        'chat/chat.html', 
        {
            'groupname': group_name,
            'chats': chats
        }
    )