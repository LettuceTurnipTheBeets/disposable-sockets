# disposable-sockets

This repository represents the full site content.

## Code

This site is developed primarily in JQuery and Bootstrap for the front-end and Python/Django/Django-Channels for the back-end.

## Technologies

The server is running the following technologies:

- Websockets

This app allows you to create disposable chat rooms where you can communicate in real-time via text chat or signatures.  The chat rooms last for 24 hours and nothing is saved after the chat room disappears.

## Extra

The cron script below runs to cleanup old images, and is located in cron.hourly/.

    find '/home/corbe054/disposable-sockets/static/images/' -mtime +0 -type f -delete

The extras/ file contains nginx, uwsgi, and systemd config files that should be placed in their appropriate folders but are saved here for revisioning.

Everything within the project is owned by www-data.  I made sure that I was a member of the sudo group as well as www-data.

UWSGI, Daphne, and django workers can be started/stopped/restarted using supervisor.

    sudo supervisorctl

Nginx can be started/stopped/restarted using systemctl.

    sudo systemctl start/stop/restart nginx
