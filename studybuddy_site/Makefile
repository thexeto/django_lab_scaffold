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

test:
- python3 manage.py test studybuddy_app

systemtest:
- python3 manage.py test studybuddy_app.tests_selenium.test_create_meetup.MySeleniumTests

pytest:
- pytest studybuddy_app/tests

pytest_all:
- pytest studybuddy_app

pytest_system:
- pytest studybuddy_app/tests_selenium

venv_install:
- ./venv/bin/pip install -r requirements.txt
