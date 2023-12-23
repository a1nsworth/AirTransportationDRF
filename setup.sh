#!/bin/bash

echo "...Creating Supper User..."

source '.env' && python manage.py createsuperuser --username=admin_root --email=admin_root@admin.com --noinput

echo "...Running Migrations..."
python manage.py makemigration
python manage.py migrate
echo "current DONE"

echo "...Starting app..."

gunicorn air_transportation.wsgi:application
