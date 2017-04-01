from rest_framework import serializers

from api.serializers.CustomerSerializer import CustomerSerializer
from api.serializers.StylistSerializer import UnNestedStylistSerializer
from core.models import Appointment


class CalendarEventSerializer(serializers.HyperlinkedModelSerializer):
    """
        The CalendarEventSerializer, like the Appointment Serializer, also references the Appointment Model.
        | The biggest differences, is that the CalendarEventSerializer can 'catch' and 'send' all the fields within the
        | Appointment Model.
        | The AppointmentSerializer, is designed only to work with only a select few fields. This was done to make
        | scheduling appointments easier, and receiving appointment information more convenient (less fields and data).
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:calendarevent-detail')

    stylist = UnNestedStylistSerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'location': {'read_only': True}
        }