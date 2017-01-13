from django.forms import ModelForm

from stylist.models import Appointments, Applications


class NewAppointmentForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ('location',)

class StylistApplicationForm(ModelForm):
    class Meta:
        model = Applications
        fields = ('reason',)