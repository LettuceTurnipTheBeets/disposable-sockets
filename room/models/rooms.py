from django.db import models
from datetime import datetime, timedelta
from room.choices import DURATION_CHOICES

class Room(models.Model):
    """Announcement model"""
    code = models.CharField(max_length=4, blank=False)
    description = models.TextField(blank=True)
    admin = models.CharField(max_length=20, blank=False)
    url = models.CharField(max_length=50, blank=False)
    #url = models.URLField(max_length=50, blank=False) # null=True
    created = models.DateTimeField(default=datetime.now())
    #duration = models.DurationField()
    #duration = models.IntegerField(default=3, choices=DURATION_CHOICES)
    name = models.CharField(max_length=40, blank=True)

    """def expires(self):
        temp = self.duration

        if temp == 1:
            return self.created + timedelta(hours=2)
        elif temp == 2:
            return self.created + timedelta(hours=6)
        elif temp == 3:
            return self.created + timedelta(hours=24)
        return self.created + duration"""

    def expires(self):
        return self.created + timedelta(hours=24)

    class Meta:
        ordering = ('created',)
