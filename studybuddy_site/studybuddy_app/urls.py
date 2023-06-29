from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:meetup_id>/", views.detail, name="detail"),
    # ex: /polls/5/rsvp/
    path("<int:meetup_id>/rsvp/", views.rsvp, name="rsvp"),
]

