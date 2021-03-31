serve:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations
gh:
	git push origin gh-pages
master:
	git push origin master
app:
	python manage.py startapp$ {{app}}
sync:
	python manage.py migrate --run-syncdb

source:
	source virtual/bin/activate

