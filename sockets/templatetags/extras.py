from sockets.models.rooms import Room
from sockets.models.guests import Guest
#from django.template.defaulttags import register
from django import template

register = template.Library()

@register.simple_tag
def get_profile_picture(code, user):
    """
    Return the user's profile picture given their name and the room code
    """
    room = Room.objects.get(code=code)
    guest = room.guests.get(user=user)

    return '/{}'.format(guest.drawing.url)
    
