from django.forms import ModelForm

from stylist.models import Appointments


class NewAppointmentForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ('location', 'date')