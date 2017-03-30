from rest_framework import serializers

from stylist.models import ShiftException


class ShiftExceptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShiftException
        fields = ('start', 'end')