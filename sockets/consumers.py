import json
from channels import Group
from sockets.models.rooms import Room
from sockets.models.chat import Chat
from django.utils import timezone
import re, io
from base64 import decodestring
from django.core.files import File
import datetime

def connect_chat(message, code):
    """
    When the user opens a WebSocket to a room stream, adds them to the
    group for that stream so they receive new post notifications.
    The notifications are actually sent in the Post model on save.
    """
    # Try to fetch the room by code; if that fails, close the socket.
    try:
        room = Room.objects.get(code=code)
    except Room.DoesNotExist:
        """
        You can see what messages back to a WebSocket look like in the spec:
        http://channels.readthedocs.org/en/latest/asgi.html#send-close
        Here, we send "close" to make Daphne close off the socket, and some
        error text for the client.
        """
        message.reply_channel.send({
            # WebSockets send either a text or binary payload each frame.
            # We do JSON over the text portion.
            "text": json.dumps({"error": "bad_slug"}),
            "close": True,
        })
        return
    message.reply_channel.send({"accept": True})
    """
    Each different client has a different "reply_channel", which is how you
    send information back to them. We can add all the different reply channels
    to a single Group, and then when we send to the group, they'll all get the
    same message.
    """
    Group(room.group_name).add(message.reply_channel)


def disconnect_chat(message, code):
    """
    Removes the user from the room group when they disconnect.
    Channels will auto-cleanup eventually, but it can take a while, and having old
    entries cluttering up your group will reduce performance.
    """
    try:
        room = Room.objects.get(code=code)
    except Room.DoesNotExist:
        # This is the disconnect message, so the socket is already gone; we can't
        # send an error back. Instead, we just return from the consumer.
        return
    # It's called .discard() because if the reply channel is already there it
    # won't fail - just like the set() type.
    Group(room.group_name).discard(message.reply_channel)


def save_post(message, code):
    """
    Saves new post to the database.
    """    
    room = Room.objects.get(code=code)
    name = json.loads(message['text'])['name']
    post = json.loads(message['text'])['post']
    now = timezone.now().replace(microsecond=0)
    if len(post) > 140:
        data_url_pattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        post = data_url_pattern.match(post).group(2)
        post = bytes(post, 'UTF-8')
        post = decodestring(post)
        img_io = io.BytesIO(post)

        obj = room.chat.create(
            name=name,
            time=now,
        )
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        obj.drawing.save('{}-{}-{}'.format(code, obj.name, time), File(img_io))
        print('file saved')
    else:
        room.chat.create(
            message=post,
            name=name,
            time=now,
        )
