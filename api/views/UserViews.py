"""
    USER VIEWS
"""
from django.contrib import auth
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import IsCurrentUserOrSuperUser
from api.utils.serializers.UserSerializer import UserSerializer
from core.models import User


@api_view(['POST', ])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
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
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
