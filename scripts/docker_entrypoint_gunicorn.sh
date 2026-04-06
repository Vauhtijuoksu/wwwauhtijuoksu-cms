#!/usr/bin/env bash
set -e

python manage.py compilemessages
python manage.py compilescss --use-storage
python manage.py collectstatic --noinput --ignore=*.scss

python manage.py migrate --noinput

# TODO: Write to file that pod is ready
touch /tmp/ready

exec "$@"
