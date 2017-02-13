import re

from django.contrib.auth import get_user_model

from core.models import User


class EmailPhoneNumberOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')

        if '@' in username and '.' in username:
            kwargs = {'email': username}
        elif phone_pattern.match(username):
            kwargs = {'phone_number': username}
        else:
            kwargs = {'username': username}

        try:
            user = UserModel.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None