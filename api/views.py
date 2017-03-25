"""
    Method views are decorated with @api_view(<Array of allowable methods>) and
    @csrf_exempt (so that the mobile app doesn't need to retrieve a csrf token before submitting a POST)

    CSRF exemption is done on the class based views by setting CsrfExemptSessionAuthentication to its list of authentication_classes
"""
from django.contrib import auth
from django.db.models import Q, Avg

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import IsOwnerOfAppointment, IsOwnerOfHaircut, IsCurrentUserOrSuperUser, IsUserLoggedIn, \
    OnlySuperUsersCanModify
from api.serializers import UserSerializer, AppointmentSerializer, PortfolioHaircutSerializer, StylistSerializer, \
    GlobalMenuSerializer, StylistMenuSerializer, ShiftSerializer, CalendarEventSerializer
from core.models import User, GlobalMenu, Appointment
from stylist.models import PortfolioHaircut, StylistMenu, Shift

'''
    USER LOGIN & LOGOUT
'''


@api_view(['POST', ])
@csrf_exempt
def user_login(request):
    """
        Simple view for user's to be able to log in.

        - **Post Params:**
            :param username: String
            :param password: String, Raw Password
            :return: Response(UserSerializer(instance=request.user, context=context).data)

        Authentication is run on the given username and password.
        If authentication is successful the user is logged in.
    """
    if request.method == 'POST':
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            context = {'request': request}
            return Response(UserSerializer(instance=request.user, context=context).data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


'''
    STYLIST SEARCH
'''


@api_view(['GET', ])
def stylist_search(request, search):
    """
        Method based view that takes a parameter called search
            :param search: http://www.<domain>.com/api/stylist_search/<search parameter goes here> | The search parameter can be any string

        If the search parameter is blank then the method returns every Stylist
        If the search parameter is not blank then the method returns every Stylist whose username, first_name, or last_name contains the parameter.
    """
    context = {'request': request}
    if request.method == 'GET':
        stylists = User.objects.filter(is_stylist='YES')

        if search == "" or search is None:
            return Response(StylistSerializer(many=True, instance=stylists, context=context).data)

        filtered_stylists = stylists.filter(
            Q(username__icontains=search) | Q(first_name__icontains=search) | Q(last_name__icontains=search))

        if len(filtered_stylists) > 0:
            return Response(StylistSerializer(many=True, instance=filtered_stylists, context=context).data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


'''
    RATING
'''


@api_view(['GET', ])
def customer_rating(request, customer_pk):
    """
        This method has a search parameter:
            :param customer_pk: The pk value of a user.

        Every user (including stylists) have a customer_rating. The customer_rating is simply the rating they get as a customer.

        | The customer's user object is pulled using the customer_pk
        | The average_rating is obtained from the average_rating field of the Customer.
        | The rating is then sent back as a JsonResponse
    """
    if request.method == 'GET':
        customer = User.objects.get(pk=int(customer_pk))
        # average_rating = Review.objects.filter(appointment__customer=customer).aggregate(Avg('customer_rating')).get('customer_rating__avg')
        average_rating = customer.average_customer_rating
        data = {'average_rating': average_rating}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def stylist_rating(request, stylist_pk):
    """
        This method has a search parameter:
            :param stylist_pk: The pk value of a stylist

        Only stylists will have a stylist_rating. Users that aren't stylists will have a default stylist_rating of zero.
        The steps to display the stylist ratings are similar to the steps that display a customer_rating.
    """
    if request.method == 'GET':
        stylist = User.objects.get(pk=int(stylist_pk))
        # average_rating = Review.objects.filter(appointment__stylist=stylist).aggregate(Avg('stylist_rating')).get('stylist_rating__avg')
        average_rating = stylist.average_stylist_rating
        data = {'average_rating': average_rating}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


'''
    USER VIEW SET
'''


class UserViewSet(viewsets.ModelViewSet):
    """
        This class handles the interactions with the User database.
        | permission_classes = (IsCurrentUserOrSuperUser)
        | authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCurrentUserOrSuperUser,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        elif user.is_anonymous:
            return None
        else:
            return User.objects.filter(email=user.email)


'''
    STYLIST VIEW SET
'''


class StylistViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
        This class handles the interactions with the Stylists in the User database. (The StylistSerializer)
        | The queryset returns all Users if their is_stylist field equals 'YES'
    """
    queryset = User.objects.all()
    serializer_class = StylistSerializer
    permission_classes = (IsUserLoggedIn,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        return User.objects.filter(is_stylist='YES')


'''
    APPOINTMENT VIEW SET
'''


class AppointmentViewSet(viewsets.ModelViewSet):
    """
        This class handles the interactions with the Appointment database.
        | The query set only returns Appointments where the stylist or customer of that appointment is the current user.
        | Before saving a new appointment the customer field is set to be the current user.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOfAppointment,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(Q(stylist=user) | Q(customer=user))

    def perform_create(self, serializer):
        """
            Before saving the Appointment the customer is set to the current user.
        """
        serializer.save(customer=self.request.user)


'''
    HAIRCUT VIEW SET
'''


class HaircutViewSet(viewsets.ModelViewSet):
    """
        This class handles the interactions with the PortfolioHaircut model.
        | It's important that a parameter is fed to the url like so:
        | http://www.<domain>.com/api/haircut?stylist_pk=1
        |   Where the stylist_pk is simply the pk value of the stylist whose haircuts you are trying to view.
        | If a stylist_pk value is not given then it will retrieve all the PortfolioHaircuts of the current user.
        |   - zero if they're a customer.
    """
    queryset = PortfolioHaircut.objects.all()
    serializer_class = PortfolioHaircutSerializer
    permission_classes = (IsOwnerOfHaircut,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        stylist = self.request.query_params.get('stylist_pk', None)
        if stylist is None:
            stylist = self.request.user
        return PortfolioHaircut.objects.filter(stylist=stylist)

    def perform_create(self, serializer):
        #Todo make it so that only Stylists can save a haircut.
        serializer.save(stylist=self.request.user)


'''
    MENU VIEW SET
'''


class GlobalMenuViewSet(viewsets.ModelViewSet):
    """
        This class handles interactions with the GlobalMenu model.
        | Nothing special here.
    """
    queryset = GlobalMenu.objects.all()
    serializer_class = GlobalMenuSerializer
    permission_classes = (OnlySuperUsersCanModify,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


class StylistMenuViewSet(viewsets.ModelViewSet):
    """
        This class handles interactions with the StylistMenu model.
        | The queryset returns all of the stylist's menu options
        | Before saving a new menu option the stylist field is set to the current user.
    """
    queryset = StylistMenu.objects.all()
    serializer_class = StylistMenuSerializer

    def get_queryset(self):
        stylist = self.request.query_params.get('stylist_pk', None)
        if stylist is None:
            stylist = self.request.user
        return StylistMenu.objects.filter(stylist=stylist)

    def perform_create(self, serializer):
        #Todo: currently there's nothing stoping customer's from creating a stylist menu option.
        serializer.save(stylist=self.request.user)


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    # permission_classes = ()
    # Need to add permissions so only Stylists can modify shift items.

    def get_queryset(self):
        stylist = self.request.query_params.get('stylist_pk', None)
        if stylist is None:
            return Shift.objects.filter(owner=self.request.user)
        else:
            return Shift.objects.filter(owner=stylist)


class CalendarEventViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = CalendarEventSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        stylist = self.request.query_params.get('stylist_pk', None)
        user = self.request.user
        return Appointment.objects.filter(Q(stylist=user) | Q(customer=user) | Q(stylist=stylist))


