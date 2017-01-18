from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.serializers import UserSerializer
from core.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # permission_classes = []
    serializer_class = UserSerializer
