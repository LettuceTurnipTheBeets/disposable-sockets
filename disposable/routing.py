from channels import route
from sockets.consumers import save_post, connect_chat, disconnect_chat

channel_routing = [
    # Called when incoming WebSockets connect
    route("websocket.connect", connect_chat, path=r'^/(?P<code>[a-zA-Z]{4})/stream/$'),

    # Called when the client closes the socket
    route("websocket.disconnect", disconnect_chat, path=r'^(?P<code>[a-zA-Z]{4})/stream/$'),

    # Called when the client sends message on the WebSocket
    route("websocket.receive", save_post, path=r'^/(?P<code>[a-zA-Z]{4})/stream/$'),
]
