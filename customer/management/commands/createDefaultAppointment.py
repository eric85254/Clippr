"""
    Creates dummy Appointments for the dummy stylist@gmail.com
    An appointment with each status is created.
    An ItemInBill entry is created for each appointment with the appointment status as its name.
"""
from datetime import datetime
from random import Random

from django.core.management import BaseCommand

from core.models import Appointment, User, ItemInBill
from customer.utils.dummy_appointment_information import appointment_information
from stylist.models import PortfolioHaircut
from stylist.utils.view_logic import BillLogic


class Command(BaseCommand):
    help = "Create Default Appointment Command"

    def handle(self, *args, **options):
        random = Random()

        stylist = User.objects.get(email="stylist@gmail.com")
        customer = User.objects.get(email="customer@gmail.com")

        haircuts = PortfolioHaircut.objects.filter(stylist=stylist)

        for item in appointment_information:
            haircut = random.choice(haircuts)
            appointment = Appointment(
                title=item.get('status'),
                location='Arizona State University',
                start_date_time=datetime.strptime(item.get('start_date_time'), '%Y-%m-%dT%H:%M'),
                end_date_time=datetime.strptime(item.get('start_date_time'), '%Y-%m-%dT%H:%M') + haircut.duration,
                stylist=stylist,
                customer=customer,
                status=item.get('status'),
            )
            appointment.save()
            ItemInBill.objects.create(
                item_portfolio=haircut,
                price=haircut.price,
                appointment=appointment
            )
            BillLogic.update_price(appointment)
