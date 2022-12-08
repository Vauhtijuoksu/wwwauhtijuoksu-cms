#!/bin/bash

if [[ $DJANGO_MIGRATE == "true" ]]; then
  python manage.py migrate --noinput
fi

touch /tmp/ready

exec "$@"
