from django.shortcuts import render

from django.http import HttpResponse

from .models import Meetup

from django.template import loader


def index(request):
    meetup_list = Meetup.objects.order_by("start_time")[:5]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/index.html", context)


def detail(request, meetup_id):
    return HttpResponse("You're looking at meeting %s." % meetup_id)


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)

