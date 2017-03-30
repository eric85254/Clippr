from rest_framework import serializers

from api.utils.serializers.ShiftExceptionSerializer import ShiftExceptionSerializer
from api.utils.serializers.StylistSerializer import StylistSerializer
from stylist.models import Shift


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:shift-detail')
    owner = StylistSerializer(many=False, read_only=True)
    pk = serializers.ReadOnlyField()
    ranges = ShiftExceptionSerializer(source='get_exceptions', many=True, read_only=True)

    class Meta:
        model = Shift
        fields = '__all__'
