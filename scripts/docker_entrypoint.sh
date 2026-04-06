#!/usr/bin/env bash

set -e
source /.venv/bin/activate

export DJANGO_SUPERUSER_USERNAME=cms
export DJANGO_SUPERUSER_PASSWORD=cms
export DJANGO_SUPERUSER_EMAIL=admin@vauhtijuoksu.fi
python manage.py migrate
python manage.py createsuperuser --noinput || true
python manage.py runserver 0.0.0.0:8000
