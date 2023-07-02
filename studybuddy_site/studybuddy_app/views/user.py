from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {"user": user}
    return render(request, "studybuddy_app/user_detail.html", context)
