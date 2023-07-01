from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from ..models import Meetup
import datetime

# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#listview


class IndexView(generic.ListView):
    template_name = "studybuddy_app/meetup_index.html"
    context_object_name = "meetup_list"
    
    def get_queryset(self):
        return Meetup.objects.filter(
            start_time__gte = timezone.now())
        
    def put(self, request, *args, **kwargs):
        return edit(request)

    def post(self, request, *args, **kwargs):
        return create(request)

    
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
    meetup_list = Meetup.objects.filter(start_time__gte = timezone.now())
    #meetup_list = Meetup.objects.order_by("start_time") # [:10]
    context = {"meetup_list": meetup_list}
    return render(request, "studybuddy_app/meetup_index.html", context)


def new(request):
    context = {"meetup": None,
               "http_method": 'POST',
               'method': 'POST',
               "action_url": reverse('studybuddy_app:meetup.path_meetups'),
               "button_text": 'Create'
               }
    return render(request, "studybuddy_app/meetup_form.html", context)

def edit(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    context = {"meetup": meetup, 
               "http_method": 'POST',
               'method': 'PUT',
               "action_url": reverse('studybuddy_app:meetup.path_meetups_pk', args=[pk]),
               "button_text": 'Save'}
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
