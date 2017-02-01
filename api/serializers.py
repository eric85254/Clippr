from rest_framework import serializers

from core.models import User, Appointment, Menu
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from stylist.models import PortfolioHaircut

'''
    User Serializer.
        Profile Pictures is FileField
        Hashed Password cannot be viewed - field is write_only
        Hashed Password is created using the create method.
'''

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail', lookup_field='username')
    profile_picture = serializers.FileField(default=DEFAULT_PICTURE_LOCATION)

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'password', 'username', 'is_stylist', 'profile_picture')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        # user.profile_picture = DEFAULT_PICTURE_LOCATION
        user.save()

        return user

'''
    Stylist Serializer.
        Similar to User Serializer, but gives
'''

class StylistSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:stylist-detail', lookup_field='username')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'username', 'profile_picture')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:appointment-detail')

    stylist = serializers.SlugRelatedField(many=False, read_only=False, slug_field=User.USERNAME_FIELD,
                                           queryset=User.objects.filter(is_stylist='YES'))
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ('url', 'location', 'date', 'stylist', 'customer')


class PortfolioHaircutSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:portfoliohaircut-detail')

    stylist = UserSerializer(many=False, read_only=True)

    class Meta:
        model = PortfolioHaircut
        fields = ('url', 'stylist', 'picture', 'name', 'description', 'price')


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:menu-detail')

    class Meta:
        model = Menu
        fields = ('url', 'name', 'category', 'price', 'picture', 'description')

