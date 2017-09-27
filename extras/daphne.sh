#!/bin/bash
# Place in /etc/rc.local
cd /home/corbe054/disposable-sockets/
source /var/env/disposable/bin/activate
daphne -b 0.0.0.0 -p 8000 disposable.asgi:channel_layer

