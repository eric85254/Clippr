from django.contrib.auth.forms import UserCreationForm

from stylist.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'is_stylist')