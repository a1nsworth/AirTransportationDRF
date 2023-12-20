#!/bin/bash

echo "...Running Migrations..."
python manage.py migrate
echo "current DONE"

echo "...Starting app..."

gunicorn air_transportation.wsgi:application
