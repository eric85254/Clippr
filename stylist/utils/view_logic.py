from django.db.models import Sum

from core.models import ItemInBill
from stylist.models import StylistMenu


class BillLogic(object):
    @staticmethod
    def update_price(appointment):
        """
            Simple method that finds all the ItemInBill entries for a particular appointment
            and then sums up the cost.
            | the appointment.price field is then updated with this newly calculated sum.
            | the appointment is then saved.
        """
        total = ItemInBill.objects.filter(appointment=appointment).aggregate(sum=Sum('price'))['sum']
        appointment.price = total
        appointment.save()

    @staticmethod
    def combine_appointment_bill(appointment_set):
        appointment_set_bill = {}
        for appointment in appointment_set:
            bill = ItemInBill.objects.filter(appointment=appointment)
            appointment_set_bill[appointment] = bill
        return appointment_set_bill


class StylistLogic(object):
    @staticmethod
    def is_stylist(request):
        if request.user.is_stylist == 'YES':
            return True
        else:
            return False
