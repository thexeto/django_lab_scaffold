
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from studybuddy_app.models import Meetup
from .helper import create_meetup, LoggedInTests


class MeetupDetailViewTests(LoggedInTests):

    def test_detail_view(self):
        meetup_1 = create_meetup(meetup_title="Future meetup 1", days=2)
        response = self.client.get(
            reverse("studybuddy_app:meetup.detail", args=[meetup_1.pk]))
        self.assertContains(response, meetup_1.title)
        
