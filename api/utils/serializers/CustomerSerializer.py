from rest_framework import serializers

from core.models import User


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
        CustomerSerializer draws from the User Model, but omits many not-needed fields.

        Use this serializer when a customer's information is needed by a stylist or another customer.
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:customer-detail')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'profile_picture')
