import random

from studybuddy_app.models import *
from django.contrib.auth.models import User

# https://django-extensions.readthedocs.io/en/latest/runscript.html#introduction
# python manage.py runscript -v3 link_fixtures


def run():
    users = list(User.objects.all())
    meetups = list(Meetup.objects.all())
    for meetup in meetups:
        participants = random.sample(users,random.randrange(2,len(users)))
        for p in participants:
            meetup.participants.add(p)
            print(f"add {p} to {meetup}")
    

    

