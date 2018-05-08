from django.db import models
from datetime import datetime, timedelta
from channels import Group

class Room(models.Model):
    """Room model"""
    code = models.CharField(max_length=4, blank=False, unique=True)
    description = models.TextField(blank=True)
    admin = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=40, blank=True)
    created = models.DateTimeField(blank=False)

    @property
    def group_name(self):
        """Returns the Channels Group name to use for sending
           notifications.
        """
        return "room-%s" % self.id

    def expires(self):
        return self.created + timedelta(hours=24)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('-id',)
