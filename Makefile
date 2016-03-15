clean:
	find . -name "*.pyc" -exec rm -rf {} \;


migrate:
	python litly/manage.py makemigrations resources
	python litly/manage.py migrate


test:
	python litly/manage.py test litly

rs:
	python litly/manage.py runserver
