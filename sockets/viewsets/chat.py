from sockets.models.chat import Chat
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'message',
            'name',
            'time',
        )
