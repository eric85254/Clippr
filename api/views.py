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
    MenuSerializer
from core.models import User, Appointment, Menu, Review
from stylist.models import PortfolioHaircut

'''
    USER LOGIN & LOGOUT
'''


@api_view(['POST', ])
@csrf_exempt
def user_login(request):
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
def my_rating(request):
    if request.method == 'GET':
        if request.user.is_stylist == 'YES':
            average_rating = Review.objects.filter(appointment__stylist=request.user).aggregate(Avg('stylist_rating'))
        elif request.user.is_stylist == 'NO':
            average_rating = Review.objects.filter(appointment__customer=request.user).aggregate(Avg('customer_rating'))
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        data = {'average_rating': average_rating.get('stylist_rating__avg')}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def customer_rating(request, customer_pk):
    if request.method == 'GET':
        customer = User.objects.get(pk=int(customer_pk))
        average_rating = Review.objects.filter(appointment__customer=customer).aggregate(Avg('customer_rating'))
        data = {'average_rating': average_rating.get('customer_rating__avg')}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def stylist_rating(request, stylist_pk):
    if request.method == 'GET':
        stylist = User.objects.get(pk=int(stylist_pk))
        average_rating = Review.objects.filter(appointment__stylist=stylist).aggregate(Avg('stylist_rating'))
        data = {'average_rating': average_rating.get('stylist_rating__avg')}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


'''
    USER VIEW SET
'''


class UserViewSet(viewsets.ModelViewSet):
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
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOfAppointment,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous or not user.is_authenticated:
            return None
        return Appointment.objects.filter(Q(stylist=user) | Q(customer=user))

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


'''
    HAIRCUT VIEW SET
'''


class HaircutViewSet(viewsets.ModelViewSet):
    queryset = PortfolioHaircut.objects.all()
    serializer_class = PortfolioHaircutSerializer
    permission_classes = (IsOwnerOfHaircut,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        return PortfolioHaircut.objects.filter(stylist=self.request.user)

    def perform_create(self, serializer):
        serializer.save(stylist=self.request.user)


'''
    MENU VIEW SET
'''


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (OnlySuperUsersCanModify,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
