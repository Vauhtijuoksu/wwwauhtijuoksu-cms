#!/usr/bin/env bash

python manage.py migrate --noinput

export DJANGO_SUPERUSER_USERNAME=cms
export DJANGO_SUPERUSER_PASSWORD=cms
export DJANGO_SUPERUSER_EMAIL=admin@vauhtijuoksu.fi
python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:8000
