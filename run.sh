#!/bin/sh
set -x


echo "==================="
echo "Running web"
echo "==================="
echo
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:9000    