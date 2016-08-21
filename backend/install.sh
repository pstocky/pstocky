#!/bin/bash

rm -f db.sqlite3

python manage.py migrate
# python manage.py createsuperuser \
#     --username=admin

python manage.py loaddata init_data/initial_data.json

rm -rf media
cp -R init_data media
