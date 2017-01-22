from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.permissions import IsOwnerOfAppointment, IsOwnerOfHaircut, IsCurrentUser
from api.serializers import UserSerializer, AppointmentSerializer, HaircutSerializer
from core.models import User
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION
from stylist.models import Appointment, Haircut


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsCurrentUser,)

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
