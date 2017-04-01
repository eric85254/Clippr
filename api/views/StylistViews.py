"""
    STYLIST VIEWS
"""

from django.db.models import Q
from rest_framework import mixins
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import IsUserLoggedIn
from api.serializers import StylistSerializer
from core.models import User


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


class StylistViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
        This class handles the interactions with the Stylists in the User database. (The StylistSerializer)
        | The queryset returns all Users if their is_stylist field equals 'YES'
    """
    queryset = User.objects.filter(is_stylist='YES')
    serializer_class = StylistSerializer
    permission_classes = (IsUserLoggedIn,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
