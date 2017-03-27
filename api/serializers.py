from rest_framework import serializers

from core.models import User, GlobalMenu, Appointment
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from stylist.models import PortfolioHaircut, StylistMenu, Shift, ShiftException

'''
    User Serializer.
        Profile Pictures is FileField
        Hashed Password cannot be viewed - field is write_only
        Hashed Password is created using the create method.
'''


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        UserSerializer (serializer for User Model)

        - **fields**::
            :url: Url for a specific object
            :first_name: First name
            :last_name: Last name
            :email: Email Address
            :phone_number: Phone Number (no dashes, spaces, or any other separators except for '+' at beginning)
            :password: Unhashed password if posting - hashed if GET ('write_only': True}
            :is_stylist: YES or NO
            :profile_picture: Profile Picture (storage type is FileField) Default is assigned here.
    """
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    profile_picture = serializers.FileField(default=DEFAULT_PICTURE_LOCATION)

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'is_stylist',
                  'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Method overrides the default create method. Ensures that password is hashed before stored."""
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        # user.profile_picture = DEFAULT_PICTURE_LOCATION
        user.save()

        return user


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

    class Meta:
        model = PortfolioHaircut
        fields = ('url', 'picture', 'name', 'description', 'price')


'''
    Menu Serializer
'''


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


'''
    Appointment Serializer
        Customer's can only pick stylists from a list of stylists hence the SlugRelatedField.
        Customer ties to UserSerializer.
'''


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

    stylist = serializers.SlugRelatedField(many=False, read_only=False, slug_field=User.USERNAME_FIELD,
                                           queryset=User.objects.filter(is_stylist='YES'))
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = (
            'url', 'title', 'location', 'start_time', 'end_time', 'start_date_time', 'end_date_time', 'stylist',
            'customer', 'status')
        extra_kwargs = {
            'status': {'read_only': True}
        }


class CalendarEventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:calendarevent-detail')

    stylist = StylistSerializer(many=False, read_only=True)
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'location': {'read_only': True}
        }


class ShiftExceptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShiftException
        fields = ('start', 'end')


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:shift-detail')
    owner = StylistSerializer(many=False, read_only=True)
    pk = serializers.ReadOnlyField()
    ranges = ShiftExceptionSerializer(source='get_exceptions', many=True, read_only=True)

    class Meta:
        model = Shift
        fields = '__all__'
