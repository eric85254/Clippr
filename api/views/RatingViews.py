"""
    RATING
"""
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import User


@api_view(['GET', ])
def customer_rating(request, customer_pk):
    """
        This method has a search parameter:
            :param customer_pk: The pk value of a user.

        Every user (including stylists) have a customer_rating. The customer_rating is simply the rating they get as a customer.

        | The customer's user object is pulled using the customer_pk
        | The average_rating is obtained from the average_rating field of the Customer.
        | The rating is then sent back as a JsonResponse
    """
    if request.method == 'GET':
        customer = User.objects.get(pk=int(customer_pk))
        # average_rating = Review.objects.filter(appointment__customer=customer).aggregate(Avg('customer_rating')).get('customer_rating__avg')
        average_rating = customer.average_customer_rating
        data = {'average_rating': average_rating}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def stylist_rating(request, stylist_pk):
    """
        This method has a search parameter:
            :param stylist_pk: The pk value of a stylist

        Only stylists will have a stylist_rating. Users that aren't stylists will have a default stylist_rating of zero.
        The steps to display the stylist ratings are similar to the steps that display a customer_rating.
    """
    if request.method == 'GET':
        stylist = User.objects.get(pk=int(stylist_pk))
        # average_rating = Review.objects.filter(appointment__stylist=stylist).aggregate(Avg('stylist_rating')).get('stylist_rating__avg')
        average_rating = stylist.average_stylist_rating
        data = {'average_rating': average_rating}
        return JsonResponse(data=data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
