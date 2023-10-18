#!/bin/sh

# clean data in database
#python manage.py flush --no-input

# migration to application
python3 django_app.py makemigrations
python3 django_app.py migrate
# collect static files
python3 django_app.py collectstatic --no-input --clear

# create superuser for postgres
# python manage.py createsuperuser --email=admin@admin.com --noinput

python3 django_app.py runserver 0.0.0.0:8000