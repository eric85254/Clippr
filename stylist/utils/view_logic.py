from django.db.models import Sum

from core.models import ItemInBill


class BillLogic(object):

    @staticmethod
    def update_price(appointment):
        total = ItemInBill.objects.filter(appointment=appointment).aggregate(sum=Sum('price'))['sum']
        appointment.price = total
        appointment.save()