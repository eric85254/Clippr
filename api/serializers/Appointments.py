from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

from api.serializers.Customer import CustomerSerializer
from api.serializers.Menus import StylistMenuSerializer
from api.serializers.PortfolioHaircuts import PortfolioHaircutSerializer
from api.serializers.User import UserSerializer
from core.models import Appointment, User, ItemInBill, GlobalMenu
from stylist.models import PortfolioHaircut, StylistMenu


class CustomPortfolioHaircutSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='api:portfoliohaircut-detail')
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=2)


class CustomStylistMenuSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='api:stylistmenu-detail')
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=2)


class ItemInBillSerializer(serializers.HyperlinkedModelSerializer):
    item_portfolio = CustomPortfolioHaircutSerializer(many=False, read_only=False, allow_null=True)
    item_menu = CustomStylistMenuSerializer(many=False, read_only=False, allow_null=True)

    class Meta:
        model = ItemInBill
        fields = (
            'item_portfolio',
            'item_menu',
        )


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    """
        AppointmentSerializer (serializer for Appointment Model)

        - **fields**::
            :url: Url for a specific object
            :location: Text field for the location
            :date: Date Field
            :stylist: SlugRelatedField (ensures that you can only select a stylist from the given options)
            :customer: UserSerialzer(many=False, read_only=True)
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:appointment-detail')

    stylist = serializers.HyperlinkedRelatedField(view_name='api:stylist-detail', many=False, read_only=False,
                                                  queryset=User.objects.filter(is_stylist='YES'))
    customer = serializers.HyperlinkedIdentityField(view_name='api:customer-detail', many=False, read_only=True)

    item_in_bill = ItemInBillSerializer(many=True, read_only=False)

    class Meta:
        model = Appointment
        fields = (
            'url',
            'title',
            'location',
            'start_date_time',
            'end_date_time',
            'stylist',
            'customer',
            'status',
            'item_in_bill',
        )

        extra_kwargs = {
            'status': {'read_only': True},
            'end_date_time': {'read_only': True},
            'title': {'read_only': True}
        }

    def create(self, validated_data):
        item_in_bill = validated_data.pop('item_in_bill')
        if len(item_in_bill) != 1:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        item_in_bill = item_in_bill.pop()
        appointment = Appointment(**validated_data)

        item_portfolio = item_in_bill.get('item_portfolio')
        item_menu = item_in_bill.get('item_menu')

        if item_portfolio:
            haircut = PortfolioHaircut.objects.get(pk=int(item_portfolio.get('pk')))
            appointment.end_date_time = appointment.start_date_time + haircut.duration
            appointment.title = haircut.name
            appointment.save()
            ItemInBill.objects.create(appointment=appointment, item_portfolio=haircut)

        elif item_menu:
            menu = StylistMenu.objects.get(pk=int(item_menu.get('pk')))
            appointment.end_date_time = appointment.start_date_time + menu.duration
            appointment.title = menu.name
            appointment.save()
            ItemInBill.objects.create(appointment=appointment, item_menu=menu)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return appointment
