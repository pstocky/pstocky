#!/bin/bash

rm -rf init_data
cp -R media init_data

python manage.py dumpdata \
    --natural-foreign \
    --exclude auth.permission --exclude admin.logentry --exclude contenttypes \
    --indent 4 \
    > init_data/initial_data.json
