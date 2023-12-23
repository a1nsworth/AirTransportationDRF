#!/bin/bash

echo "...Creating Supper User..."

python manage.py createsuperuser --username=admin --email=admin@admin.com --noinput

echo "...Running Migrations..."
python manage.py makemigration
python manage.py migrate
echo "current DONE"

echo "...Starting app..."

gunicorn air_transportation.wsgi:application
