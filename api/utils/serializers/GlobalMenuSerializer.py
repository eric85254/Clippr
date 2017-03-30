from rest_framework import serializers

from core.models import GlobalMenu


class GlobalMenuSerializer(serializers.HyperlinkedModelSerializer):
    """
        GlobalMenuSerializer (serializer for GlobalMenu Model)

        - **fields**::
            :url: Url for a specific object
            :name: CharField
            :price: DecimalField
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:globalmenu-detail')

    class Meta:
        model = GlobalMenu
        fields = ('url', 'name', 'price')