"""
    HAIRCUT VIEW SET
"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import IsOwnerOfHaircut
from api.utils.serializers import PortfolioHaircutSerializer
from stylist.models import PortfolioHaircut


class HaircutViewSet(viewsets.ModelViewSet):
    """
        This class handles the interactions with the PortfolioHaircut model.
        | It's important that a parameter is fed to the url like so:
        | http://www.<domain>.com/api/haircut?stylist_pk=1
        |   Where the stylist_pk is simply the pk value of the stylist whose haircuts you are trying to view.
        | If a stylist_pk value is not given then it will retrieve all the PortfolioHaircuts of the current user.
        |   - zero if they're a customer.
    """
    queryset = PortfolioHaircut.objects.all()
    serializer_class = PortfolioHaircutSerializer
    permission_classes = (IsOwnerOfHaircut,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        stylist = self.request.query_params.get('stylist_pk', None)
        if stylist is None:
            stylist = self.request.user
        return PortfolioHaircut.objects.filter(stylist=stylist)

    def perform_create(self, serializer):
        # Todo make it so that only Stylists can save a haircut.
        serializer.save(stylist=self.request.user)
