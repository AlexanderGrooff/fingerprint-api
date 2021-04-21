#!/usr/bin/env bash
python manage.py migrate
gunicorn --bind :3000 --workers 3 fingerprint_api.wsgi:application
