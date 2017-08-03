from api.models.rooms import Room
from api.viewsets.chat import ChatSerializer
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view


class RoomSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(many=True, required=False)

    def update(self, code, validated_data):
        chat_data = validated_data
        room = Room.objects.get(code=code)
        Chat.objects.create(room=room, **chat_data)
        return room

    class Meta:
        model = Room
        fields = (
            'id',
            'admin',
            'chat',
            'code',
            'created',
            'description',
            'expires',
            'name',
            'url',
        )

        
class RoomViewSet(viewsets.ModelViewSet):
    """
    Django Rest Framework Room ViewSet
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @api_view(['put'])
    def update(self, request, pk=None):
        pass
    
    @api_view(['patch'])
    def partial_update(self, request, pk=None):
        pass

    @api_view(['delete'])
    def destroy(self, request, pk=None):
        pass
