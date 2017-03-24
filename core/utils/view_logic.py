"""
    This class contains a series of common methods that are utilized throughout the core app.
"""
from django.contrib import auth
from django.db.models import Avg
from django.shortcuts import redirect

from core.forms import UserInformation
from core.models import Review


class UserLogic(object):
    """
        Common methods relating to User
    """
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
        """
            Directs the user to the proper dashboard or profile page depending on their is_stylist or superuser status.
        """
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

    #Todo: Should remove this method
    @staticmethod
    def upload_picture(request):
        """
        Redundant - should remove.
        """
        user = request.user
        user.profile_picture = request.FILES['profile_picture']
        user.save()

    #Todo: Make this documentation a bit clearer.
    @staticmethod
    def update_average(review):
        """
            This method is called whenever a new review is made.
            | It takes the given review and pulls the stylist and customer users from it.
            | Then every review pertaining to the customer and stylist is pulled.
            | The ratings of all these reviews are averaged then stored to the stylist's or customer's average rating field.
        """
        stylist = review.appointment.stylist
        customer = review.appointment.customer

        stylist.average_stylist_rating = Review.objects.filter(appointment__stylist=stylist).aggregate(
            Avg('stylist_rating')).get('stylist_rating__avg')
        customer.average_customer_rating = Review.objects.filter(appointment__customer=customer).aggregate(
            Avg('customer_rating')).get('customer_rating__avg')

        stylist.save()
        customer.save()


class CookieClearer(object):
    """
        This class is important because of how cookies are used. For example, the stylist_pk is stored in a cookie and is used
        to retrieve the stylist and the stylist's information at different pages. However, this same cookie might be used in a different setting,
        a setting where you might not want to see the same stylist that you scheduled the appointment with.

        | After a big function (such as creating an appointment) is completed the cookies are all cleared by invoking the method in this class.
    """
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
                del request.session[name]
