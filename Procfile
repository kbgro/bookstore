release: python manage.py migrate
release: python manage.py loaddata data.json
web: gunicorn bookstore_project.wsgi --log-file -
