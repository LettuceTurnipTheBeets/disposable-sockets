start on runlevel [2345]
stop on runlevel [016]

respawn

script
    cd /home/corbe054/disposable-sockets/
    export DJANGO_SETTINGS_MODULE="disposable.settings"
    exec daphne -b 0.0.0.0 -p 8000 disposable.asgi:channel_layer
end script
