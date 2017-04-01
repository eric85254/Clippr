"""
    CUSTOMER VIEW SET
"""
from rest_framework import viewsets

from api.utils.serializers import CustomerSerializer
from core.models import User


class CustomerViewSet(viewsets.ModelViewSet):
    """
        This class renders information about a particular customer.

        todo: Need to build validation to ensure that super users or staff don't show up on this viewset.
    """

    queryset = User.objects.filter(is_stylist='NO')
    serializer_class = CustomerSerializer