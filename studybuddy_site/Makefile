.PHONY : django migrate
.RECIPEPREFIX = -

venv=.venv_studybuddy
port=8000
python=./${venv}/bin/python

django:
- open http://127.0.0.1:${port}/studybuddy
- ${python} manage.py runserver ${port}

makemigration:
- ${python} manage.py makemigrations studybuddy_app

migrate:
- ${python} manage.py migrate

admin:
- open http://127.0.0.1:${port}/admin

django_source:
- code /Library/Frameworks/Python.framework/Versions/3.11/lib/${python}.11/site-packages/django

open:
- open http://127.0.0.1:8000/studybuddy

test:
- ${python} manage.py test studybuddy_app

test_unit:
- ${python} manage.py test studybuddy_app/tests

systemtest:
- ${python} manage.py test studybuddy_app.tests_selenium.test_create_meetup.MySeleniumTests

pytest:
- ${python} -m pytest studybuddy_app/tests

pytest_all:
- ${python} -m pytest studybuddy_app

pytest_system:
- ${python} -m pytest studybuddy_app/tests_selenium

venv_install:
- ${python} -m pip install -r requirements.txt

load_fixtures:
- ${python} manage.py loaddata studybuddy_app/fixtures/user.yaml
- ${python} manage.py loaddata studybuddy_app/fixtures/meetup.yaml
- ${python} manage.py runscript -v2 link_fixtures

dump_fixtures:
- ${python} manage.py dumpdata --natural-foreign --format yaml studybuddy_app
- ${python} python manage.py dumpdata auth.User --natural-primary --format yaml