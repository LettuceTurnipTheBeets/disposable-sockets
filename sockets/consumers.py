from channels.generic.websockets import WebsocketDemultiplexer

from sockets.models.integervalues import IntegerValueBinding


class Demultiplexer(WebsocketDemultiplexer):
    consumers = {
        "intval": IntegerValueBinding.consumer,
    }

    groups = ["binding.values"]
