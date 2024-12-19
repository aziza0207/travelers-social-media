#!/bin/sh

sleep 10

until nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 1
done

python manage.py flush --no-input
python manage.py migrate
python manage.py create_default_admin
python manage.py fetch_countries
python manage.py collectstatic --no-input --clear
gunicorn root.wsgi:application --bind 0.0.0.0:8000