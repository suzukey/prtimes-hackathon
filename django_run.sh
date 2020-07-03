#!/bin/bash

until python manage.py inspectdb > /dev/null 2>&1; do
  >&2 echo "Database is unavaliable"
  sleep 3
done

>&2 echo "Database is up"

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata companys.json

python manage.py runserver 0.0.0.0:8000