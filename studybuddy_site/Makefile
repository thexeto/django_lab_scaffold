.PHONY : django migrate
.RECIPEPREFIX = -

port=4711

django:
- open http://127.0.0.1:${port}/buddy
- python3 manage.py runserver ${port}

makemigration:
- python3 manage.py makemigrations studybuddy_app

migrate:
- python3 manage.py migrate

admin:
- open http://127.0.0.1:${port}/admin