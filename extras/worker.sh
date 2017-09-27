#!/bin/bash
# Place in /etc/rc.local
cd /home/corbe054/disposable-sockets/
source /var/env/disposable/bin/activate
python manage.py runworker
