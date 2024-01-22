#!/usr/bin/env bash

python manage.py compilescss --use-storage
python manage.py collectstatic --noinput --ignore=*.scss
python manage.py migrate --noinput
