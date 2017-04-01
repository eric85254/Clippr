from rest_framework import serializers

from api.serializers.UserSerializer import UserSerializer
from core.models import Appointment, User


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    """
        AppointmentSerializer (serializer for Appointment Model)

        - **fields**::
            :url: Url for a specific object
            :location: Text field for the location
            :date: Date Field
            :stylist: SlugRelatedField (ensures that you can only select a stylist from the given options)
            :customer: UserSerialzer(many=False, read_only=True)
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:appointment-detail')

    stylist = serializers.SlugRelatedField(many=False, read_only=False, slug_field=User.USERNAME_FIELD,
                                           queryset=User.objects.filter(is_stylist='YES'))
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = (
            'url',
            'title',
            'location',
            'start_time',
            'end_time',
            'start_date_time',
            'end_date_time',
            'stylist',
            'customer',
            'status',
        )

        extra_kwargs = {
            'status': {'read_only': True}
        }
