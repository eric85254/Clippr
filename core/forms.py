from django.contrib.auth.forms import UserCreationForm

from core.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'phone_number', 'is_stylist')