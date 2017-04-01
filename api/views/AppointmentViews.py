"""
    APPOINTMENT & CALENDAR VIEWS
"""
from datetime import timedelta, datetime

from django.db.models import Q
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import detail_route, authentication_classes, api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.backends import CsrfExemptSessionAuthentication
from api.permissions import IsOwnerOfAppointment
from api.serializers import AppointmentSerializer
from api.serializers import CalendarEventSerializer
from api.serializers import ShiftSerializer
from core.models import Appointment
from customer.utils.view_logic import CustomerLogic
from stylist.models import ShiftException, Shift
from stylist.utils.view_logic import StylistLogic


class AppointmentViewSet(viewsets.ModelViewSet):
    """
        This class handles the interactions with the Appointment database.
        | The query set only returns Appointments where the stylist or customer of that appointment is the current user.
        | Before saving a new appointment the customer field is set to be the current user.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (IsOwnerOfAppointment,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(Q(stylist=user) | Q(customer=user))

    def perform_create(self, serializer):
        """
            Before saving the Appointment the customer is set to the current user.
        """
        serializer.save(customer=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Appointment.STATUS_DECLINED
        instance.save()


class CalendarEventViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
        This view set handles all the information going to a person's calendar except for Shifts.
        Any modifications that need to be done to the appointments such as: rescheduling, accepting, declining, and completing
        are all done through this viewset. This view set has a couple of additional views 'accept' and 'complete'

        More information on routers can be found in the django rest framework documentation.

        Returns all the appointments that you are involved in. If a stylist_pk query paramter is sent then it returns
        all the appointments that you and the stylist you chose are involved in.

        YOU CANNOT POST TO THIS VIEW - Posting implies the creation on appointment. Must be done with AppointmentViewSet.
    """
    queryset = Appointment.objects.all()
    serializer_class = CalendarEventSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    @detail_route(methods=['PUT', ])
    def accept(self, request, pk=None):
        """
            Reached by {% url 'api:calendarevent-accept' %} or by <domain>.com/api/calendar_event/pk/accept
        """
        appointment = self.get_object()
        if StylistLogic.is_stylist(request) and (
                        appointment.status != Appointment.STATUS_ACCEPTED and appointment.status != Appointment.STATUS_COMPLETED):
            appointment.status = Appointment.STATUS_ACCEPTED
            appointment.save()
            return Response(status=status.HTTP_202_ACCEPTED)

    @detail_route(methods=['PUT', ])
    def complete(self, request, pk=None):
        """
            Reached by {% url 'api:calendarevent-complete' %} or by <domain>.com/api/calendar_event/pk/complete
        """
        appointment = self.get_object()
        if StylistLogic.is_stylist(request) and appointment.status == Appointment.STATUS_ACCEPTED:
            appointment.status = Appointment.STATUS_COMPLETED
            appointment.save()
            return Response(status=status.HTTP_202_ACCEPTED)

    def get_queryset(self):
        """
            Reached by {% url 'api:calendarevent-list' %}
        """
        stylist = self.request.query_params.get('stylist_pk', None)
        user = self.request.user
        return Appointment.objects.filter(
            Q(stylist=user) | Q(customer=user) | Q(stylist=stylist) | Q(customer=stylist)).exclude(
            status=Appointment.STATUS_DECLINED)

    def perform_update(self, serializer):
        """
            Reached by a PUT request on the detail view of a specific calendarevent.
        """
        if self.get_object().status != Appointment.STATUS_COMPLETED:
            if StylistLogic.is_stylist(self.request):
                serializer.save(status=Appointment.STATUS_RECHEDULED_BYSTYLIST)
            if CustomerLogic.is_customer(self.request):
                serializer.save(status=Appointment.STATUS_RESCHEDULED_BYCUSTOMER)

    def perform_destroy(self, instance):
        """
            Reached by a DELETE request on the detail view of a specific calendarevent.
        """
        if self.get_object().status != Appointment.STATUS_COMPLETED:
            instance.status = Appointment.STATUS_DECLINED
            instance.save()


@api_view(['POST', ])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def exclude_date(request):
    """
        Reached by {% url 'api:exclude_date' %}

        SEND PK VALUE OF SHIFT TO THIS ENDPOINT!

        This endpoint modifies and creates a new shift exception entry so that the excluded date is not
        contained within the range of valid dates for rendering.
    """
    shift = Shift.objects.get(pk=int(request.data.get('shift_pk', '')))
    number_of_exceptions = ShiftException.objects.filter(shift=shift).count()

    if (shift.dow is not None and shift.dow != "") and (number_of_exceptions != 0):
        exceptions = ShiftException.objects.filter(shift=shift)
        excluded_date = datetime.date(datetime.strptime(request.data.get('excluded_date', ''), "%Y-%m-%d"))

        exception_pk = None
        for exception in exceptions:
            if (exception.end >= excluded_date) and (excluded_date >= exception.start):
                exception_pk = exception.pk
                break

        break_point_exception = ShiftException.objects.get(pk=exception_pk)

        ShiftException.objects.create(
            shift=shift,
            start=excluded_date + timedelta(days=1),
            end=break_point_exception.end
        )
        break_point_exception.end = request.data.get('excluded_date', '')
        break_point_exception.save()

        return Response(status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        # else:
        #     return Response(status=status.HTTP_403_FORBIDDEN)


class ShiftViewSet(viewsets.ModelViewSet):
    """
        View set to obtain all shift information of a specific stylist.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # permission_classes = ()
    # Need to add permissions so only Stylists can modify shift items.

    def get_queryset(self):
        stylist = self.request.query_params.get('stylist_pk', None)
        if stylist is None:
            return Shift.objects.filter(owner=self.request.user)

        else:
            return Shift.objects.filter(owner=stylist)

    def perform_create(self, serializer):
        shift = serializer.save(owner=self.request.user)
        ShiftException.objects.create(
            shift=shift,
            start=shift.start_date_time,
            end=shift.start_date_time + timedelta(weeks=2600)
        )
