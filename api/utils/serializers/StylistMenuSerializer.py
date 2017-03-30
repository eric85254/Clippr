from rest_framework import serializers

from core.models import GlobalMenu
from stylist.models import StylistMenu


class StylistMenuSerializer(serializers.HyperlinkedModelSerializer):
    """
        StylistMenuSerializer (serializer for StylistMenu Model)

        - **fields**::
            :url: Url for a specific object
            :name: CharField
            :price: DecimalField
            :modified_global: SlugRelatedField to GlobalMenu.objects.all() slug_field='name' allow_null=True
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:stylistmenu-detail')
    modified_global = serializers.SlugRelatedField(many=False, read_only=False, allow_null=True, slug_field='name',
                                                   queryset=GlobalMenu.objects.all())

    class Meta:
        model = StylistMenu
        fields = ('url', 'name', 'price', 'modified_global')