#!/bin/bash
python -m ensurepip --upgrade
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
