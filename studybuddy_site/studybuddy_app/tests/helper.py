import datetime
from django.utils import timezone
from studybuddy_app.models import Meetup
from django.contrib.auth import get_user_model
from django.test import TestCase


def create_meetup(meetup_title, meetup_location="Room 11", days=2):
    start_time = timezone.now() + datetime.timedelta(days=days)
    duration = timezone.timedelta(hours=1)
    return Meetup.objects.create(
        title=meetup_title,
        location=meetup_location,
        start_time=start_time,
        duration=duration)


def create_user():
    u = get_user_model()(
        username='test_user',
        email='e@mail.com',
        password='geheim12')
    u.save()
    return u


class LoggedInTests(TestCase):
    def setUp(self) -> None:
        u = create_user()
        self.client.force_login(user=u)

