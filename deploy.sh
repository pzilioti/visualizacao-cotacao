#!/bin/bash
python manage.py makemigrations visualiza
python manage.py test visualiza
status=$?

if [ $status -eq 0 ]; then
	echo "Tests run sucessfully"
	docker build -t zilioti.dev/visualizacao_cotacao .
	docker-compose up -d
else
	echo "Failure. Aborting"
	exit 1
fi
