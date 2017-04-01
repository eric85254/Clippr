from rest_framework import serializers

from stylist.models import ShiftException


class ShiftExceptionSerializer(serializers.HyperlinkedModelSerializer):
    """
        This serializer is linked to the ShiftException model, and is utilized to both create a new ShiftException,
        | and by the ShiftSerializer.
    """
    class Meta:
        model = ShiftException
        fields = ('start', 'end')