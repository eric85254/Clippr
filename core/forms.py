from django.contrib.auth.forms import UserCreationForm

from stylist.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_stylist')