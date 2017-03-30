from rest_framework import serializers

from api.utils.serializers.StylistSerializer import StylistSerializer
from api.utils.serializers.UserSerializer import UserSerializer
from core.models import Appointment


class CalendarEventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:calendarevent-detail')

    stylist = StylistSerializer(many=False, read_only=True)
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'location': {'read_only': True}
        }