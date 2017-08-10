from django.db import models
from sockets.models.rooms import Room
from datetime import datetime

class Chat(models.Model):
    """
    Chat model
    """
    room = models.ForeignKey('sockets.Room', db_column='room_id', related_name='chat')
    name = models.CharField(max_length=40)
    message = models.TextField(max_length=140)
    time = models.DateTimeField(blank=False)

    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ('-time',)
