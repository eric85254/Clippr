from django.contrib import auth
from django.shortcuts import redirect

from core.forms import UserInformation


class UserLogic(object):
    @staticmethod
    def retrieve_user(request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        return user

    @staticmethod
    def login(request, user):
        if user is not None:
            auth.login(request, user)

    @staticmethod
    def redirect_to_profile(request):
        user = request.user
        if user.is_anonymous:
            request.session['error'] = "username or password is incorrect"
            return redirect('core:home_login')

        elif user.is_superuser:
            return redirect('administration:profile')

        else:
            if user.is_stylist == 'YES':
                return redirect('stylist:profile')
            else:
                return redirect('customer:profile')

    @staticmethod
    def upload_picture(request):
        user = request.user
        user.profile_picture = request.FILES['profile_picture']
        user.save()
