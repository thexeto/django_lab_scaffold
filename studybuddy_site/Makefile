.PHONY : django migrate
.RECIPEPREFIX = -

port=4711

django:
- open http://127.0.0.1:${port}/buddy
- python3 manage.py runserver ${port}

migrate:
- python manage.py migrate

admin:
- open http://127.0.0.1:${port}/admin