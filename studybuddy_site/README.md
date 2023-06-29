## Part 1

    django-admin startproject studybuddy-site
    cd studybuddy_site
    python manage.py startapp studybuddy_app

    python manage.py migrate
    python manage.py runserver

    python manage.py createsuperuser

## Part 2

    python manage.py makemigrations studybuddy_app
    python manage.py sqlmigrate studybuddy_app 0001
    python manage.py migrate