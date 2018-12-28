#!/bin/bash


cd /home/ubuntu/sites/jianyang995.com/Personal-Website/
git pull

../env/bin/pip install -r requirements.txt
../env/bin/python manage.py collectstatic --noinput
../env/bin/python manage.py migrate

sudo service nginx reload
../env/bin/gunicorn --bind unix:/tmp/jianyang995.com.socket mysite.wsgi:application&
