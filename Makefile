run:
	python3 manage.py makemigrations
	python3 manage.py migrate

server:
	python3 manage.py runserver

super:
	dropdb tour_api
	python3 manage.py createsuperuser

db:
	# dropdb tour_api
	createdb tour_api