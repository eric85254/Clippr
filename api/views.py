from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.permissions import IsOwnerOfAppointment, IsOwnerOfHaircut
from api.serializers import UserSerializer, AppointmentSerializer, HaircutSerializer
from core.models import User
from stylist.models import Appointments, Haircut


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = []
    serializer_class = UserSerializer

class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOfAppointment,)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous or not user.is_authenticated:
            return None
        return Appointments.objects.filter(Q(stylist=user) | Q(customer=user))

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class HaircutViewSet(viewsets.ModelViewSet):
    queryset = Haircut.objects.all()
    serializer_class = HaircutSerializer
    permission_classes = (IsOwnerOfHaircut,)