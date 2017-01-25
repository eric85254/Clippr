from django.forms import ModelForm

from stylist.models import Appointment, Application


class NewAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('location',)

class StylistApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('reason',)