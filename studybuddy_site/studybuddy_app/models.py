# Models: https://docs.djangoproject.com/en/4.2/topics/db/models/
# Fields: https://docs.djangoproject.com/en/4.2/ref/models/fields/

from django.db import models
from django.contrib.auth.models import User


class Meetup(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField("start time")
    end_time = models.DateTimeField("end time", blank=True)

    # participants = models.models.ManyToManyField(User)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

# many_to_many: https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/
# user objects: https://docs.djangoproject.com/en/4.2/topics/auth/default/#user-objects
