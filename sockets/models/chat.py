from django.db import models
from sockets.models.rooms import Room
from sockets.models.guests import Guest
from datetime import datetime
from channels import Group
import json


class Chat(models.Model):
    """
    Chat model
    """
    room = models.ForeignKey('sockets.Room', db_column='room_id', related_name='chat')
    name = models.CharField(max_length=40)
    message = models.TextField(max_length=140)
    drawing = models.ImageField(upload_to='static/images/', default='static/images/no-img.jpg')
    time = models.DateTimeField(blank=False)

    def __str__(self):
        return self.message
    
    def send_notification(self):
        """
        Sends a notification to everyone in our Liveblog's group with our
        content.
        """
        # Make the payload of the notification. We'll JSONify this, so it has
        # to be simple types, which is why we handle the datetime here.
        notification = {
            "id": self.id,
            "name": self.name,
            "message": self.message,
            "time": self.time.strftime("%a %d %b %-I:%M %p"),
            "drawing_url": self.drawing.url,
        }
        # Encode and send that message to the whole channels Group for our
        # liveblog. Note how you can send to a channel or Group from any part
        # of Django, not just inside a consumer.
        Group(self.room.group_name).send({
            # WebSocket text frame, with JSON content
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        """
        Hooking send_notification into the save of the object as I'm not
        the biggest fan of signals.
        """
        result = super(Chat, self).save(*args, **kwargs)
        self.send_notification()
        return result

    class Meta:
        ordering = ('time',)
