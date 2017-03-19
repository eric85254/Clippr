"""
    Forms are a class that can be utilized within a django template to quickly render the correct fields.
    They can also be utilized to catch data from a POST.
"""
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from core.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'phone_number', 'is_stylist')


class UserInformation(ModelForm):
    """
        This is how the user can change their basic information.
    """
    #Todo: You need to remember why this is here.
    def is_valid(self, *args, **kwargs):
        """
            I forgot what this does. But it's pretty important.
        """
        valid = super(UserInformation, self).is_valid()

        request = kwargs.pop('request')
        user = request.user

        # I think if the user.email is the same as the 'change' then there's an error. So this exists to override the error.
        # But the errors from the other sections can be 'hidden' if the following two lines pass.
        if user.email == self.data['email']:
            if user.phone_number == self.data['phone_number']:
                return True
        else:
            return valid


    class Meta:
        model = User
        fields = ('location', 'biography', 'hair_type', 'email', 'phone_number')
