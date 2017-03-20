from django.db.models import Sum

from core.models import ItemInBill


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