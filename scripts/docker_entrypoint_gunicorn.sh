#!/bin/bash


echo "Waiting for postgres..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py compilescss --use-storage
python manage.py collectstatic --noinput --ignore=*.scss

python manage.py migrate --noinput

# TODO: Write to file that pod is ready
touch /tmp/ready

exec "$@"
