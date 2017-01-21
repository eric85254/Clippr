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

    stylist = UserSerializer(many=False)
    customer = UserSerializer(many=False)

    class Meta:
        model = Appointments
        fields = ('url', 'location', 'date', 'stylist', 'customer')

class HaircutSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:haircut-detail')

    class Meta:
        model = Haircut
        fields = ('url', 'haircut_stylist', )