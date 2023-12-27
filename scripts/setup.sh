#!/bin/sh

echo "...Creating Supper User..."

python manage.py createsuperuser --username=admin_root --email=admin_root@admin.com --noinput

echo "...Running Migrations..."
python manage.py makemigrations
python manage.py migrate
echo "current DONE"

echo "...Starting app..."

/backup.sh
/planner.sh

gunicorn air_transportation.wsgi:application

