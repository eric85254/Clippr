"""
    HAIRCUT VIEW SET
"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import IsOwnerOfHaircut
from api.serializers import PortfolioHaircutSerializer
from customer.utils.view_logic import CustomerLogic
from stylist.models import PortfolioHaircut
from stylist.utils.view_logic import StylistLogic


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
        user = self.request.query_params.get('stylist_pk', None)
        if user is None:
            if StylistLogic.is_stylist(self.request):
                user = self.request.user
                return PortfolioHaircut.objects.filter(stylist=user)
            if CustomerLogic.is_customer(self.request):
                user = self.request.user
                return PortfolioHaircut.objects.filter(item_portfolio__appointment__customer=user).distinct()
        else:
            return PortfolioHaircut.objects.filter(stylist=user)

    def perform_create(self, serializer):
        serializer.save(stylist=self.request.user)
