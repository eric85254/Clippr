from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from core.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'phone_number', 'is_stylist')


class UserInformation(ModelForm):
    def is_valid(self, *args, **kwargs):
        valid = super(UserInformation, self).is_valid()

        request = kwargs.pop('request')
        user = request.user

        if user.email == self.data['email']:
            if user.phone_number == self.data['phone_number']:
                return True
        else:
            return valid


    class Meta:
        model = User
        fields = ('location', 'biography', 'hair_type', 'email', 'phone_number')
