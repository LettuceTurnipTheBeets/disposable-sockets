import json
from channels import Group
from sockets.models.rooms import Room
from sockets.models.chat import Chat
from sockets.helpers import now

def connect_blog(message, code):
    """
    When the user opens a WebSocket to a liveblog stream, adds them to the
    group for that stream so they receive new post notifications.
    The notifications are actually sent in the Post model on save.
    """
    # Try to fetch the liveblog by slug; if that fails, close the socket.
    try:
        room = Room.objects.get(code=code)
    except Room.DoesNotExist:
        # You can see what messages back to a WebSocket look like in the spec:
        # http://channels.readthedocs.org/en/latest/asgi.html#send-close
        # Here, we send "close" to make Daphne close off the socket, and some
        # error text for the client.
        message.reply_channel.send({
            # WebSockets send either a text or binary payload each frame.
            # We do JSON over the text portion.
            "text": json.dumps({"error": "bad_slug"}),
            "close": True,
        })
        return
    message.reply_channel.send({"accept": True})
    # Each different client has a different "reply_channel", which is how you
    # send information back to them. We can add all the different reply channels
    # to a single Group, and then when we send to the group, they'll all get the
    # same message.
    Group(room.group_name).add(message.reply_channel)

def save_post(message, code):
    """
    Saves new post to the database.
    """
    post = json.loads(message['text'])['post']
    room = Room.objects.get(code=code)
    name = json.loads(message['text'])['name']

    room.chat.create(
        message=post,
        name=name,
        time=now(),
    )
