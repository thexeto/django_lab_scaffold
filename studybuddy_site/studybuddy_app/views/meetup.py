
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib import messages
from ..forms import MeetupForm
from ..models import Meetup
from studybuddy_app.common.date import date_from_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class MeetupListView(LoginRequiredMixin, generic.ListView):
    model = Meetup

    def get_queryset(self):
        return Meetup.objects.filter(
            start_time__gte=timezone.now())

    def post(self, request, *args, **kwargs):
        return _create(request)


class MeetupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Meetup
    
    def get_context_data(self, **kwargs):
        context = super(MeetupDetailView, self).get_context_data(**kwargs)
        meetup = self.get_object()
        participants = meetup.participants.all()
        context['participants'] = participants

        return context

    def post(self, request, *args, **kwargs):
        meetup = self.get_object()
        return _update(request, meetup)


def path_meetups_pk(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    if request.method == 'GET':
        return _detail(request, meetup)
    elif request.method == 'POST':
        return _update(request, meetup)
    elif request.method == 'DELETE':
        return delete(request, meetup)
    raise Http404("Page not found.")


@login_required
def new(request):
    meetup = Meetup()
    meetup_form = MeetupForm(instance=meetup)
    context = {"meetup": None,
               "meetup_form": meetup_form,
               "http_method": 'POST',
               "action_url": reverse('studybuddy_app:meetup.path_meetups'),
               "button_text": 'Create'
               }
    return render(request, "studybuddy_app/meetup_form.html", context)


@login_required
def edit(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    return _render_meetup_form(request, meetup=meetup, pk=pk)


def _render_meetup_form(request, meetup=None, old_meetup_form=None, pk=None):
    if pk is None:
        action_url = reverse('studybuddy_app:meetup.path_meetups')
    else:
        action_url = reverse(
            'studybuddy_app:meetup.path_meetups_pk',
            args=[pk])
        
    if old_meetup_form is None:
        meetup_form = MeetupForm(instance=meetup)
    else:
        meetup_form = old_meetup_form
        
    context = {"meetup": meetup,
               "http_method": 'POST',
               "meetup_form": meetup_form,
               "action_url": action_url,
               "button_text": 'Save'}
    return render(request, "studybuddy_app/meetup_form.html", context)


def _save_meetup(meetup_form):
    if not meetup_form.is_valid():
        return None
    meetup = meetup_form.save(commit=False)
    meetup.start_time = date_from_form(meetup.start_time)
    meetup.save()
    return meetup


def _create(request):
    # title = request.POST["title"]
    # meetup = Meetup(title=title,
    #                 start_time=timezone.now() + datetime.timedelta(days=1))
    # meetup.save()
    # return HttpResponseRedirect(
    #     reverse("studybuddy_app:meetup.path_meetups_pk",
    #             args=[meetup.id]))
    meetup_form = MeetupForm(request.POST, request.FILES)
    meetup = _save_meetup(meetup_form=meetup_form)
    if meetup:
        messages.success(request, ('Your meetup was successfully added!'))

        return HttpResponseRedirect(
            reverse("studybuddy_app:meetup.path_meetups_pk",
                    args=[meetup.id]))
    else:
        messages.error(request, 'Error saving form')
        return _render_meetup_form(request, old_meetup_form=meetup_form)


def _update(request, meetup):
    meetup_form = MeetupForm(request.POST, instance=meetup)
    meetup = _save_meetup(meetup_form=meetup_form)
    if meetup:
        messages.success(request, ('Your meetup was successfully _updated!'))
        #return _render_meetup(request, meetup)
        return HttpResponseRedirect(
            reverse("studybuddy_app:meetup.path_meetups_pk",
                    args=[meetup.id]))
    else:
        messages.error(request, 'Error saving form')
        return _render_meetup_form(request, meetup=meetup)


def _render_meetup(request, meetup):
    context = {"meetup": meetup}
    return render(request, "studybuddy_app/meetup_detail.html", context)


def _detail(request, meetup):
    context = {"meetup": meetup,
               "view": "detail"}
    return render(request, "studybuddy_app/meetup_detail.html", context)

@login_required
def delete(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    meetup.delete()
    return HttpResponseRedirect(
        reverse("studybuddy_app:meetup.path_meetups"))

@login_required
def rsvp(request, pk):
    if request.user.is_authenticated:
        meetup = Meetup.objects.get(pk=pk)
        meetup.participants.add(request.user)
    return HttpResponseRedirect(
            reverse("studybuddy_app:meetup.path_meetups_pk",
                    args=[meetup.id]))
