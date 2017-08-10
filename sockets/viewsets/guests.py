from sockets.models.guests import Guest
from rest_framework import serializers


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = (
            'user',
        )
