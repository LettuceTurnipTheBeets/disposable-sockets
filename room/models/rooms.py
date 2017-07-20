from django.db import models
from datetime import datetime


class Room(models.Model):
    """Announcement model"""
    code = models.CharField(max_length=4, blank=False)
    description = models.TextField(blank=True)
    admin = models.CharField(max_length=20, blank=False)
    url = models.URLField(max_length=50, blank=False) # null=True
    date_created = models.DateTimeField(default=datetime.now())
    duration = models.DurationField()
    name = models.CharField(max_length=40, blank=True)


    def date_expires(self):
        return self.date_created + duration

    class Meta:
        db_table = 'rooms'
        verbose_name = 'Room'
        app_label = 'rooms'
