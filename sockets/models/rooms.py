from django.db import models
from datetime import datetime, timedelta
from sockets.choices import DURATION_CHOICES

class Room(models.Model):
    """
    Room model
    """
    code = models.CharField(max_length=4, blank=False, unique=True)
    description = models.TextField(blank=True)
    admin = models.CharField(max_length=20, blank=False)
    created = models.DateTimeField(blank=False)
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

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('-id',)
