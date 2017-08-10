from sockets.models.rooms import Room
from sockets.viewsets.chat import ChatSerializer
from sockets.viewsets.guests import GuestSerializer
from rest_framework import serializers, viewsets
import django_filters


class RoomFilter(django_filters.rest_framework.FilterSet):
    """
    Filter on code, created, expires
    """
    class Meta:
        model = Room
        fields = {
            'code': ['exact'],
            'created': ['lt', 'gt', 'lte', 'gte', 'exact', 'contains'],
            'id': ['lt', 'gt', 'lte', 'gte', 'exact'],
            #'expires': ['lt', 'gt', 'lte', 'gte', 'exact', 'contains'],
        }

class RoomSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(many=True, required=False, read_only=True)
    guests = GuestSerializer(many=True, required=False, read_only=True)

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
            'guests',
            'name',
            'url',
        )

        
class RoomViewSet(viewsets.ModelViewSet):
    """
    Django Rest Framework Room ViewSet
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_class = RoomFilter
