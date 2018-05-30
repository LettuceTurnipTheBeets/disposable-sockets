# disposable-sockets

This app allows you to create disposable chat rooms where you can communicate in real-time via text chat or signatures.  The chat rooms last for 24 hours and nothing is saved after the chat room disappears.

## Code

This site is developed primarily in JQuery and Bootstrap for the front-end and Python/Django/Django-Channels for the back-end.

## Websockets

The server is leveraging websockets through django-channels.

## Requirements

asgi-redis 1.4.2  
channels 1.1.6  
Django 1.11.3  
django-crontab 0.7.1  
mysqlclient 1.3.10  
pytz 2017.2  
Pillow 4.2.1  

## Extra

The cron script below runs to cleanup old images, and is located in cron.hourly/.

    find '~/disposable-sockets/static/images/' -mtime +0 -type f -delete

The extras/ file contains nginx, uwsgi, and systemd config files that should be placed in their appropriate folders but are saved here for revisioning.

Everything within the project is owned by www-data.  I made sure that I was a member of the sudo group as well as www-data.

UWSGI, Daphne, and django workers can be started/stopped/restarted using supervisor.

    sudo supervisorctl

Nginx can be started/stopped/restarted using systemctl.

    sudo systemctl start/stop/restart nginx
