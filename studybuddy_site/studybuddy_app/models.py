# Models: https://docs.djangoproject.com/en/4.2/topics/db/models/
# Fields: https://docs.djangoproject.com/en/4.2/ref/models/fields/

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField("start time")
    end_time = models.DateTimeField("end time", null=True, blank=True)

    participants = models.ManyToManyField(User)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def is_upcoming(self):
        soon = timezone.now() + datetime.timedelta(days=2)
        return self.start_time >= timezone.now() and self.start_time <= soon


# many_to_many: https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
# user objects: https://docs.djangoproject.com/en/4.2/topics/auth/default/#user-objects
# timezone https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/
