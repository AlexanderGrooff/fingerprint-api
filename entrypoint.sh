#!/usr/bin/env bash
python manage.py migrate
./manage.py runserver localhost:3000
