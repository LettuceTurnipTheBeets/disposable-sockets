from sockets.models.rooms import Room
from django.utils import timezone


def delete_expired_rooms():
    """
    Check if a room has expired and if so delete it.
    If this changes you need to run 'python manage.py crontab show/add/remove'
    """
    rooms = Room.objects.all()
    now = timezone.now()

    for date in rooms:
        if now > date.expires():
            date.delete()

"""def delete_expired_images():
   Delete all images older than 1 day.  This is run as a cron job with the source below:
   find '/home/corbe054/disposable-sockets/static/images/' -mtime +0 -type f -delete
"""

