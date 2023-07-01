from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

from .models import Meetup


def index(request):
    meetup_list = Meetup.objects.order_by("start_time")[:10]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/meetup_index.html", context)


def detail(request, meetup_id):
    meetup = get_object_or_404(Meetup, pk=meetup_id)
    context = {"meetup": meetup}
    return render(request, "studybuddy_app/meetup_detail.html", context)


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)


# if request.method =='POST':  # comes here when you are making a post request via submitting the form
#         # Register user
#         redirect()
#     else:  # if you are making a get request, then code goes to this block
#         return render(request,'accounts/register.html')  # this is for rendering the html page when you hit the url