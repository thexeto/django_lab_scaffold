import datetime
from django import forms
from django.db import models
from .models import Meetup 
from django.utils import timezone
from django.forms.renderers import TemplatesSetting

# https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#validation-on-a-modelform

class CustomFormRenderer(TemplatesSetting):
    form_template_name = "studybuddy_app/form_snippet.html"
    
class MeetupForm(forms.ModelForm):
    error_css_class = "error"
    required_css_class = "required"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm"})
    class Meta:
        model = Meetup
        exclude = ()
        #tomorrow = timezone.now() + datetime.timedelta(days=1)
        #tomorrow_p2 = tomorrow + datetime.timedelta(hours=2)
        #start_time = forms.DateTimeField(initial=tomorrow)
        #end_time = forms.DateTimeField(initial=tomorrow_p2)
        #
        #title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"))
        #location = forms.CharField(max_length=100)
        ##fields = ('title', 'location', 'start_time', 'end_time') 
        #exclude = ()
        

       
   