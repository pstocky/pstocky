#!/bin/bash

if [ ! -n "$1" ]; then
    port=8000
else
    port=$1
fi

python manage.py runserver 0.0.0.0:$port
