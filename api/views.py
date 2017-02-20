from django.contrib import auth
from django.db.models import Q

# Create your views here.
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.permissions import IsOwnerOfAppointment, IsOwnerOfHaircut, IsCurrentUserOrSuperUser, IsUserLoggedIn, \
    OnlySuperUsersCanModify
from api.serializers import UserSerializer, AppointmentSerializer, PortfolioHaircutSerializer, StylistSerializer, \
    MenuSerializer
from core.models import User, Appointment, Menu
from stylist.models import PortfolioHaircut

'''
    USER LOGIN & LOGOUT
'''

@api_view(['POST', ])
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
    USER VIEW SET
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCurrentUserOrSuperUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(username=user.username)

'''
    STYLIST VIEW SET
'''

class StylistViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = StylistSerializer
    permission_classes = (IsUserLoggedIn,)

    def get_queryset(self):
        return User.objects.filter(is_stylist='YES')

'''
    APPOINTMENT VIEW SET
'''

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOfAppointment,)

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

