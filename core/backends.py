import re

from django.contrib.auth import get_user_model

from core.models import User


class EmailPhoneNumberOrUsernameModelBackend(object):
    """
        A custom backend created to by pass the traditional username & password login.
        | This backend allows the user to login with either a phone number or an email address.
        | The phone_number or email is still sent through the 'username' parameter
        | The code utilizes regex to identify a phone_number and a simpler check for email address.
        | Once the username is correctly identified as either a phone_number or email address the user model is pulled and the password is checked.
    """
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')

        if '@' in username and '.' in username:
            kwargs = {'email': username}
        elif phone_pattern.match(username):
            kwargs = {'phone_number': username}
        else:
            kwargs = {'username': None}

        try:
            user = UserModel.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    #Todo: learn what this method does.
    def get_user(self, username):
        """
            Not entirely sure what this does. Found it on stackoverflow and it seemed to have fixed my issue.
        """
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None