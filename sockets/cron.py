from sockets.models.rooms import Room
from django.utils import timezone


def delete_expired_rooms():
    rooms = Room.objects.all()
    now = timezone.now()

    for date in rooms:
        if now > date.expires():
            date.delete()
