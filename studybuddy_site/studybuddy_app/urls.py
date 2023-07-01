from django.urls import path
from . import views as meetup_views
from . import user_views


app_name = "studybuddy_app"

urlpatterns = [
    path("", meetup_views.index, name="index"),
    # ex: /buddy/5/
    path("<int:meetup_id>/", meetup_views.detail, name="meetup.detail"),
    # ex: /buddy/5/rsvp/
    path("<int:meetup_id>/rsvp/", meetup_views.rsvp, name="meetup.rsvp"),
    path("user/<int:pk>", user_views.detail, name="user.detail")
]
