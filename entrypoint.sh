#!/usr/bin/env bash

set -e
set -x

echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py collectstatic --clear --no-input
python manage.py migrate
gunicorn -c gunicorn.conf.py fingerprint_api.wsgi:application
