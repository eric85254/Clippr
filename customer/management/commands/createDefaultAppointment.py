from django.core.management import BaseCommand

from core.models import Appointment, User, ItemInBill
from stylist.utils.view_logic import BillLogic


class Command(BaseCommand):
    help = "Create Default Appointment Command"

    def handle(self, *args, **options):
        stylist = User.objects.get(email="stylist@gmail.com")
        customer = User.objects.get(email="customer@gmail.com")

        statuses = [
            Appointment.STATUS_PENDING,
            Appointment.STATUS_RECHEDULED_BYSTYLIST,
            Appointment.STATUS_RESCHEDULED_BYCUSTOMER,
            Appointment.STATUS_ACCEPTED,
            Appointment.STATUS_DECLINED,
            Appointment.STATUS_COMPLETED
        ]

        for status in statuses:
            appointment = Appointment(
                stylist=stylist,
                customer=customer,
                location="Arizona State University",
                status=status
            )
            appointment.save()
            ItemInBill.objects.create(
                item_custom=status,
                price=42.00,
                appointment=appointment
            )
            BillLogic.update_price(appointment)
