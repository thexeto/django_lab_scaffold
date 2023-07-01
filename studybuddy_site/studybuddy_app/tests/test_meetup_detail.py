
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from studybuddy_app.models import Meetup


def create_meetup(meetup_title, meetup_location="Room 11", days=2):
    start_time = timezone.now() + datetime.timedelta(days=days)
    end_time = start_time + datetime.timedelta(hours=2)
    return Meetup.objects.create(
        title=meetup_title,
        location=meetup_location,
        start_time=start_time,
        end_time=end_time)


class MeetupDetailViewTests(TestCase):
    def test_detail_view(self):
        meetup_1 = create_meetup(meetup_title="Future meetup 1", days=2)
        response = self.client.get(
            reverse("studybuddy_app:meetup.path_meetups_pk", args=[meetup_1.pk]))
        self.assertContains(response, meetup_1.title)
        
