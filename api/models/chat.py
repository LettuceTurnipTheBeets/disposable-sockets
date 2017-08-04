from django.db import models
from api.models.rooms import Room
from datetime import datetime

class Chat(models.Model):
    """
    Chat model
    """
    room = models.ForeignKey('api.Room', db_column='room_id', related_name='chat')
    name = models.CharField(max_length=40)
    message = models.TextField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ('-time',)
