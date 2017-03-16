from django.db.models import Sum

from core.models import ItemInBill


class BillLogic(object):
    @staticmethod
    def update_price(appointment):
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
