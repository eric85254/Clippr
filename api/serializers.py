from rest_framework import serializers

from core.models import User
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from stylist.models import Appointment, Haircut


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


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:appointments-detail')

    stylist = serializers.SlugRelatedField(many=False, read_only=False, slug_field=User.USERNAME_FIELD,
                                           queryset=User.objects.filter(is_stylist='YES'))
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ('url', 'location', 'date', 'stylist', 'customer')


class HaircutSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:haircut-detail')

    haircut_stylist = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Haircut
        fields = ('url', 'haircut_stylist', 'haircut_picture', 'haircut_name', 'haircut_description')
