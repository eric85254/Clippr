from rest_framework import serializers

from stylist.models import PortfolioHaircut

'''
    PortfolioHaircut Serializer
    To get a specific stylist haircut use: http://127.0.0.1:8000/api/haircut/?stylist_pk=1
'''


class PortfolioHaircutSerializer(serializers.HyperlinkedModelSerializer):
    """
        PortfolioHaircutSerializer (serializer for PortfolioHaircut Model)

        - **fields**::
            :url: Url for a specific object
            :stylist: StylistSerializer(many=False, read_only=True)
            :picture: FileField?
            :name: CharField
            :description: TextField or CharField
            :price: DecimalField
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:portfoliohaircut-detail')
    pk = serializers.ReadOnlyField()

    class Meta:
        model = PortfolioHaircut
        fields = ('pk', 'url', 'picture', 'name', 'description', 'price')

