from room.models.rooms import Room
from rest_framework import serializers, viewsets


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('code', 'url', 'description', 'admin', 'date_created', 'duration', 'date_expires', 'name')

        
class RoomViewSet(viewsets.ModelViewSet):
    """
    Django Rest Framework Room ViewSet
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

