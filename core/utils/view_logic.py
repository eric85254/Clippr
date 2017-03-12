from django.contrib import auth
from django.db.models import Avg
from django.shortcuts import redirect

from core.forms import UserInformation
from core.models import Review


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
    def redirect_to_dashboard(request):
        user = request.user
        if user.is_anonymous:
            request.session['error'] = "username or password is incorrect"
            return redirect('core:home_login')

        elif user.is_superuser:
            return redirect('administration:profile')

        else:
            if user.is_stylist == 'YES':
                return redirect('stylist:dashboard')
            else:
                return redirect('customer:dashboard')

    @staticmethod
    def upload_picture(request):
        user = request.user
        user.profile_picture = request.FILES['profile_picture']
        user.save()

    @staticmethod
    def update_average(review):
        stylist = review.appointment.stylist
        customer = review.appointment.customer

        stylist.average_stylist_rating = Review.objects.filter(appointment__stylist=stylist).aggregate(
            Avg('stylist_rating')).get('stylist_rating__avg')
        customer.average_customer_rating = Review.objects.filter(appointment__customer=customer).aggregate(
            Avg('customer_rating')).get('customer_rating__avg')

        stylist.save()
        customer.save()


class CookieClearer(object):
    @staticmethod
    def appointment_cookies(request):
        cookie_names = [
            'portfolio_haircut',
            'stylist_option_pk',
            'stylist_pk',
            'menu_main'
        ]

        CookieClearer.clear(cookie_names, request)

    # Helper Method
    @staticmethod
    def clear(cookie_names, request):
        for name in cookie_names:
            if name in request.session:
                request.session[name] = None
