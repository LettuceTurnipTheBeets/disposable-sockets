from channels import include


channel_routing = [
    include("sockets.routing.websocket_routing", path=r"^/sockets"),
]
