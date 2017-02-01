from rest_framework import serializers

from core.models import User, Appointment
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from stylist.models import PortfolioHaircut


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail', lookup_field='username')
    profile_picture = serializers.FileField(default=DEFAULT_PICTURE_LOCATION)

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'username', 'password', 'is_stylist', 'profile_picture')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        # user.profile_picture = DEFAULT_PICTURE_LOCATION
        user.save()

        return user


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

