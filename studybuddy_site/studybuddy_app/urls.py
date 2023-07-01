from django.urls import path
from .views import user as user_views
from .views import meetup as meetup_views

app_name = "studybuddy_app"

urlpatterns = [
    path("", meetup_views.index, name="index"),
    path("<int:pk>/", meetup_views.detail, name="meetup.detail"),
    path("<int:pk>/rsvp/", meetup_views.rsvp, name="meetup.rsvp"),

    path("meetups", meetup_views.path_meetups, name="meetup.index"),
    path("meetups/<int:pk>/",
         meetup_views.path_meetups_pk, name="meetup.detail"),
    path("meetups/new", meetup_views.new, name="meetup.new"),
    path("meetups/<int:pk>/edit", meetup_views.edit, name="meetup.edit"),

    path("users/<int:pk>", user_views.detail, name="user.detail")
]

# https://restfulapi.net/
# https://apiguide.readthedocs.io/en/latest/build_and_publish/use_RESTful_urls.html

# list: GET /meetups
# create meetup: POST /meetups

# single meetup: GET /meetups/:id
# update meetup: PUT /meetups/:id
# delete meetup: DELETE /meetups/:id

# new form: GET /meetups/new
# edit form: GET /meetups/:id/edit
