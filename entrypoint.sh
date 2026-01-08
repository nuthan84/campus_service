#!/bin/sh
python manage.py migrate
gunicorn campus_service.wsgi --bind 0.0.0.0:$PORT
