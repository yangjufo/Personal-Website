#!/bin/bash

source_folder=/home/ubuntu/sites/www.jianyang995.com

cd $source_folder/Personal-Website
git reset *
git pull
sed -i 's/DEBUG = True/DEBUG = False/' ./mysite/settings.py

$source_folder/env/bin/pip install -r requirements.txt --no-cache-dir
$source_folder/env/bin/python manage.py collectstatic --noinput
$source_folder/env/bin/python manage.py migrate

sudo service nginx reload
$source_folder/env/bin/gunicorn --bind unix:/tmp/www.jianyang995.com.socket mysite.wsgi:application&
