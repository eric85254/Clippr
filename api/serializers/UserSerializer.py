from rest_framework import serializers
from core.models import User
from core.utils.picture_locations import DEFAULT_PICTURE_LOCATION

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
