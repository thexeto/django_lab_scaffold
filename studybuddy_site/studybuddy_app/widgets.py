from django.forms.widgets import Input, DateTimeInput
from studybuddy_app.common.date import date_to_form

# https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
class HTML5DateTimeInput(DateTimeInput):

    input_type = 'datetime-local'
    supports_microseconds = False

    def format_value(self, value):
        """ returns a value for use in the widget template.
        """
        return date_to_form(value)
