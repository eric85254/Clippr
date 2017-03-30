from rest_framework import serializers

from api.utils.serializers.PortfolioHaircutSerializer import PortfolioHaircutSerializer
from api.utils.serializers.StylistMenuSerializer import StylistMenuSerializer
from core.models import User

'''
    Stylist Serializer.
        Similar to User Serializer but omits many unnecessary fields.
        Since the model is User, by default it utilizes user-* views. Conflicts with User views.
            Thus base_name = 'stylist' in urls.py
'''


class StylistSerializer(serializers.HyperlinkedModelSerializer):
    """
        StylistSerializer (serializer for User Model) Omits many unneeded fields of the User Model.

        Fields are not listed because corresponding view should not accept POST, PUT, or DELETE.
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:stylist-detail')
    portfolio_haircuts = PortfolioHaircutSerializer(source='get_portfolio_haircuts', many=True, read_only=True)
    stylist_menu = StylistMenuSerializer(source='get_stylist_menu', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'profile_picture', 'portfolio_haircuts', 'stylist_menu')
