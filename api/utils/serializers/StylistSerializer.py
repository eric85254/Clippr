from rest_framework import serializers

from api.utils.serializers.PortfolioHaircutSerializer import PortfolioHaircutSerializer
from api.utils.serializers.StylistMenuSerializer import StylistMenuSerializer
from core.models import User

'''
    Stylist Serializer.
'''


class StylistSerializer(serializers.HyperlinkedModelSerializer):
    """
        StylistSerializer (serializer for User Model) Omits many unneeded fields of the User Model.

        Since the model is User, by default it utilizes user-* views. Conflicts with User views.
            Thus base_name = 'stylist' in urls.py

        This serializer also has a couple of additional fields such as portfolio_haircuts and stylist_menu.
        | This is so that separate requests to the portfolio_haircut and stylist_menu api pages are not needed.
        | This serializer should be used whenever a customer is trying to view information about a stylist.
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:stylist-detail')
    portfolio_haircuts = PortfolioHaircutSerializer(source='get_portfolio_haircuts', many=True, read_only=True)
    stylist_menu = StylistMenuSerializer(source='get_stylist_menu', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'profile_picture', 'portfolio_haircuts', 'stylist_menu')


class UnNestedStylistSerializer(serializers.HyperlinkedModelSerializer):
    """
        The StylistSerializer has a couple serializers nested within it that are unnecessary for the
        FullCalendar.

        This class was made specifically for the CalendarEventSerializer.

        not that the url links to the stylist-detail.
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:stylist-detail')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'profile_picture')