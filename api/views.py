from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.permissions import IsOwnerOfAppointment, IsOwnerOfHaircut, IsCurrentUser
from api.serializers import UserSerializer, AppointmentSerializer, HaircutSerializer
from core.models import User
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from stylist.models import Appointment, Haircut


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCurrentUser,)
    lookup_field = 'username'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(username=user.username)


class AppointmentsViewSet(viewsets.ModelViewSet):
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


class HaircutViewSet(viewsets.ModelViewSet):
    queryset = Haircut.objects.all()
    serializer_class = HaircutSerializer
    permission_classes = (IsOwnerOfHaircut,)

    def get_queryset(self):
        return Haircut.objects.filter(haircut_stylist=self.request.user)

    def perform_create(self, serializer):
        serializer.save(haircut_stylist=self.request.user)
