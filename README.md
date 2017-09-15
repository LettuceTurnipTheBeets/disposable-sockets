# disposable-sockets

This repository represents the full site content.

## Code

This site is developed primarily in JQuery and Bootstrap for the front-end and Python/Django/Django-Channels for the back-end.

## Technologies

The server is running the following technologies:

- Websockets

This app allows you to create disposable chat rooms where you can communicate in real-time via text chat or signatures.  The chat rooms last for 24 hours and nothing is saved after the chat room disappears.

## Extra

The cron script that runs to cleanup old images is:
    find '/home/corbe054/disposable-sockets/static/images/' -mtime +0 -type f -delete

The extras/ file contains nginx, uwsgi, and systemd config files that should be placed in their appropriate folders but are saved here for revisioning.
