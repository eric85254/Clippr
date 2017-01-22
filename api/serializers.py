from rest_framework import serializers

from core.models import User
from stylist.models import Appointments, Haircut


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'username', 'password', 'is_stylist')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:appointments-detail')

    stylist = serializers.SlugRelatedField(many=False, read_only=False, slug_field=User.USERNAME_FIELD,
                                           queryset=User.objects.filter(is_stylist='YES'))
    customer = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Appointments
        fields = ('url', 'location', 'date', 'stylist', 'customer')


class HaircutSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:haircut-detail')

    haircut_stylist = serializers.SlugRelatedField(many=False, read_only=False, slug_field=User.USERNAME_FIELD,
                                                   queryset=User.objects.all())

    class Meta:
        model = Haircut
        fields = ('url', 'haircut_stylist', 'haircut_picture', 'haircut_name', 'haircut_description')
