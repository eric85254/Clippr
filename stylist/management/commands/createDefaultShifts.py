"""
    Creates a dummy shift schedule for a dummy stylist
"""
from django.core.management import BaseCommand

from core.models import User
from stylist.models import Shift


class Command(BaseCommand):
    help = "create dummy shift schedule for stylist@gmail.com... create the dummy account first!"

    def handle(self, *args, **options):
        stylist = User.objects.get(email="stylist@gmail.com")

        DAYS = [
            Shift.MONDAY,
            Shift.TUESDAY,
            Shift.WEDNESDAY,
            Shift.THURSDAY,
            Shift.FRIDAY
        ]

        for day in DAYS:
            Shift.objects.create(
                owner=stylist,
                title="available",
                start_time="8:00:00",
                end_time="14:00:00",
                dow="[" + str(day) + "]",
            )
