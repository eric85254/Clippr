from django.core.management import BaseCommand

from core.models import Appointment, User, ItemInBill
from stylist.utils.view_logic import BillLogic


class Command(BaseCommand):
    help = "Create Default Appointment Command"

    def handle(self, *args, **options):
        stylist = User.objects.get(email="stylist@gmail.com")
        customer = User.objects.get(email="customer@gmail.com")

        appointment = Appointment(
            stylist=stylist,
            customer=customer,
            location="Arizona State University",
            status=Appointment.STATUS_PENDING
        )
        appointment.save()
        ItemInBill.objects.create(
            item_custom="DEFAULT APPOINTMENT CREATED",
            price=42.00,
            appointment=appointment
        )
        BillLogic.update_price(appointment)
