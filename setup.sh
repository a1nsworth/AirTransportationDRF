#!/bin/bash

echo "...Creating Supper User..."

python manage.py createsuperuser --noinput --username $root --email $- --password $root

echo "...Running Migrations..."
python manage.py migrate
echo "current DONE"

echo "...Starting app..."

gunicorn air_transportation.wsgi:application
