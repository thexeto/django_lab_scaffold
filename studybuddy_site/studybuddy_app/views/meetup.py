from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

from ..models import Meetup


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
    elif request.method == 'PUT':
        return update(request, meetup)
    elif request.method == 'DELETE':
        return delete(request, meetup)
    raise Http404("Page not found.")


def index(request):
    meetup_list = Meetup.objects.order_by("start_time")[:10]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/meetup_index.html", context)


def new(request):
    context = {"meetup": None,
               "http_method": 'POST',
               "action_url": 'studybuddy_app:meetup.index',
               "action_id": None,
               "button_text": 'Create'
               }
    return render(request, "studybuddy_app/meetup_form.html", context)


def create(request):
    context = {"meetup": None,
               "view": "create"}
    return render(request, "studybuddy_app/meetup_detail.html", context)


def update(request, meetup):
    meetup.title = request.POST["title"]
    meetup.save
    context = {"meetup": meetup,
               "dict": request.POST,
               "view": "update"
               }
    return render(request, "studybuddy_app/meetup_detail.html", context)


def edit(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    context = {"meetup": meetup, 
               "http_method": 'PUT',
               "action_url": 'studybuddy_app:meetup.detail',
               "action_id": pk,
               "button_text": 'Save'}
    return render(request, "studybuddy_app/meetup_form.html", context)


def detail(request, meetup):
    context = {"meetup": meetup,
               "view": "detail"}
    return render(request, "studybuddy_app/meetup_detail.html", context)


def delete(request, meetup):
    context = {"meetup": meetup} 
    return HttpResponse("delete meetup")


def rsvp(request, meetup_id):
    return HttpResponse("You rsvp on meetup %s." % meetup_id)


# if request.method =='POST':  # comes here when you are making a post request via submitting the form
#         # Register user
#         redirect()
#     else:  # if you are making a get request, then code goes to this block
#         return render(request,'accounts/register.html')  # this is for rendering the html page when you hit the url
