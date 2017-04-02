from rest_framework import serializers

from api.serializers.ShiftExceptionSerializer import ShiftExceptionSerializer
from api.serializers.StylistSerializer import UnNestedStylistSerializer
from stylist.models import Shift


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    """
        This serializer is used to retrieve shift schedules for stylists for FullCalendar.
        This serializer also pulls all the ShiftExceptions associated with a particular Shift - These are read-only.
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:shift-detail')
    owner = UnNestedStylistSerializer(many=False, read_only=True)
    pk = serializers.ReadOnlyField()
    ranges = ShiftExceptionSerializer(source='get_exceptions', many=True, read_only=True)

    class Meta:
        model = Shift
        fields = '__all__'