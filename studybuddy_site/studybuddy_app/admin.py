from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Meetup


# admin.site.register(Meetup)

class MeetupAdmin(admin.ModelAdmin):
    # fields = ["location", "title", "start_time", "end_time"]
    
    fieldsets = [
        (None, {"fields": ["location", "title"]}),
        ("Date information", {"fields": ["start_time", "end_time"]}),
    ]
    list_display = ["title", "start_time"]


admin.site.register(Meetup, MeetupAdmin)
