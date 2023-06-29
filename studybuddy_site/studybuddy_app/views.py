from django.shortcuts import render

from django.http import HttpResponse

from .models import Meetup


def index(request):
    next_meetups_list = Meetup.objects.order_by("start_time")[:5]
    output = "Hello, world. You're at the studybuddy index."
    output += ", ".join([m.title for m in next_meetups_list])
    return HttpResponse(output)


def detail(request, meetup_id):
    return HttpResponse("You're looking at meeting %s." % meetup_id)


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)

