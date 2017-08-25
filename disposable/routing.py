from channels import route
from sockets.consumers import save_post, connect_blog


# The channel routing defines what channels get handled by what consumers,
# including optional matching on message attributes. In this example, we route
# all WebSocket connections to the class-based BindingConsumer (the consumer
# class itself specifies what channels it wants to consume)
channel_routing = [
    # Called when incoming WebSockets connect - liveblog
    route("websocket.connect", connect_blog, path=r'^/(?P<code>[a-zA-Z]{4})/stream/$'),

    # Called when the client closes the socket - liveblog
    # route("websocket.disconnect", disconnect_blog, path=r'^(?P<code>[a-zA-Z]{4})/stream/$'),

    # Called when the client sends message on the WebSocket - liveblog
    route("websocket.receive", save_post, path=r'^/(?P<code>[a-zA-Z]{4})/stream/$'),

    # A default "http.request" route is always inserted by Django at the end of the routing list
    # that routes all unmatched HTTP requests to the Django view system. If you want lower-level
    # HTTP handling - e.g. long-polling - you can do it here and route by path, and let the rest
    # fall through to normal views.
]
