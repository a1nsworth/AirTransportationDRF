#!/bin/bash

echo "...Running Migrations..."
python manage.py makemigrations
echo "current DONE"

echo "...Starting app..."

gunicorn air_transportation.wsgi:application
