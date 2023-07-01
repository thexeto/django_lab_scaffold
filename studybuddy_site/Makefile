.PHONY : django migrate
.RECIPEPREFIX = -

port=4711

django:
- open http://127.0.0.1:${port}/studybuddy
- python3 manage.py runserver ${port}

makemigration:
- python3 manage.py makemigrations studybuddy_app

migrate:
- python3 manage.py migrate

admin:
- open http://127.0.0.1:${port}/admin

django_source:
- code /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/django

open:
- open http://127.0.0.1:8000/studybuddy
