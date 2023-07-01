# Models: https://docs.djangoproject.com/en/4.2/topics/db/models/
# Fields: https://docs.djangoproject.com/en/4.2/ref/models/fields/

import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from .widgets import HTML5DateTimeInput

# https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.from_db_value
   
   
class ConvertingDateTimeField(models.DateTimeField):
    widget = HTML5DateTimeInput
  
    def to_python(self, value):
        if type(value) == str:
            date_time = datetime.datetime.fromisoformat(value)
            value = date_time.isoformat(' ', timespec='minutes')
        return value


def tomorrow():
    return timezone.now() + datetime.timedelta(days=1)

# https://docs.djangoproject.com/en/4.2/ref/models/fields/#integerfield
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#durationfield
# https://docs.python.org/3/library/datetime.html#datetime.timedelta


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    start_time = ConvertingDateTimeField("start time", default=tomorrow)
    duration = models.DurationField(default=datetime.timedelta(hours=1))
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
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
