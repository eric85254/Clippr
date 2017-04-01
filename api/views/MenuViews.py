"""
    MENU VIEW SET
"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import OnlySuperUsersCanModify
from api.utils.serializers import GlobalMenuSerializer
from api.utils.serializers import StylistMenuSerializer
from core.models import GlobalMenu
from stylist.models import StylistMenu


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
        # Todo: currently there's nothing stoping customer's from creating a stylist menu option.
        serializer.save(stylist=self.request.user)