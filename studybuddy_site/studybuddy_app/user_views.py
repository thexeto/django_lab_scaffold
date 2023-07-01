from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model


def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {"user": user}
    return render(request, "studybuddy_app/user_detail.html", context)

