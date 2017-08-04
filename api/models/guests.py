from django.db import models
from api.models.rooms import Room

class Guest(models.Model):
    """
    Guest model
    """
    room = models.ForeignKey('api.Room', db_column='room_id', related_name='guests')
    user = models.CharField(max_length=40)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ('user',)
