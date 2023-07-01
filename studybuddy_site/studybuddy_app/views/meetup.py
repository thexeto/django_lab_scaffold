from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone

from ..models import Meetup
import datetime


def path_meetups(request):
    if request.method == 'GET':
        return index(request)
    elif request.method == 'POST':
        return create(request)
    raise Http404("Page not found.")


def path_meetups_pk(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    if request.method == 'GET':
        return detail(request, meetup)
    elif request.method == 'POST':
        return update(request, meetup)
    elif request.method == 'DELETE':
        return delete(request, meetup)
    raise Http404("Page not found.")


def index(request):
    meetup_list = Meetup.objects.order_by("start_time") # [:10]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/meetup_index.html", context)


def new(request):
    context = {"meetup": None,
               "http_method": 'POST',
               "action_url": reverse('studybuddy_app:meetup.path_meetups'),
               "button_text": 'Create'
               }
    return render(request, "studybuddy_app/meetup_form.html", context)


def create(request):
    title = request.POST["title"]
    meetup = Meetup(title=title,
                    start_time=timezone.now() + datetime.timedelta(days=1))
    meetup.save()
    return HttpResponseRedirect(
        reverse("studybuddy_app:meetup.path_meetups_pk",
                args=[meetup.id]))


def update(request, meetup):
    meetup.title = request.POST["title"]
    meetup.save()
    return HttpResponseRedirect(
        reverse("studybuddy_app:meetup.path_meetups_pk",
                args=[meetup.id]))


def edit(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    context = {"meetup": meetup, 
               "http_method": 'POST',
               "action_url": reverse('studybuddy_app:meetup.path_meetups_pk', args=[pk]),
               "button_text": 'Save'}
    return render(request, "studybuddy_app/meetup_form.html", context)


def detail(request, meetup):
    context = {"meetup": meetup,
               "view": "detail"}
    return render(request, "studybuddy_app/meetup_detail.html", context)


def delete(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    meetup.delete()
    return index(request)


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)


# if request.method =='POST':  # comes here when you are making a post request via submitting the form
#         # Register user
#         redirect()
#     else:  # if you are making a get request, then code goes to this block
#         return render(request,'accounts/register.html')  # this is for rendering the html page when you hit the url
