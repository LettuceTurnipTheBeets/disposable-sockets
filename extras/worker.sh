#!/bin/bash
cd /home/corbe054/disposable-sockets/
source /var/env/disposable/bin/activate
python manage.py runworker
