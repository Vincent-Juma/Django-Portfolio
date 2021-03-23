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