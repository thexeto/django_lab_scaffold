from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Meetup



def index(request):
    meetup_list = Meetup.objects.order_by("start_time")[:5]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/index.html", context)


def detail(request, meetup_id):
    try: 
        meetup = Meetup.objects.get(pk=meetup_id)
    except Meetup.DoesNotExist:
        raise Http404(f"Meetup {meetup_id} not found.")
    context = {"meetup": meetup}
    return render(request, "studybuddy_app/detail.html", context)


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)

