from django.views import generic
from .models import Course


class CourseListView(generic.ListView):
    model = Course
