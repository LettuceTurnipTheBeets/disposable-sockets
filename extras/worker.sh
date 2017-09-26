start on runlevel [2345]
stop on runlevel [016]

respawn

script
    cd /home/corbe054/disposable-sockets/
    export DJANGO_SETTINGS_MODULE="disposable.settings"
    exec python manage.py runworker
end script
