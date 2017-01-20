from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.permissions import IsMemberOfAppointment
from api.serializers import UserSerializer, AppointmentSerializer
from core.models import User
from stylist.models import Appointments


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = []
    serializer_class = UserSerializer

class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsMemberOfAppointment,)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous or not user.is_authenticated:
            return None
        return Appointments.objects.filter(Q(stylist=user) | Q(customer=user))