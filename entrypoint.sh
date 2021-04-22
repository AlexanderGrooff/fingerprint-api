#!/usr/bin/env bash
python manage.py migrate
gunicorn -c gunicorn.conf.py fingerprint_api.wsgi:application
