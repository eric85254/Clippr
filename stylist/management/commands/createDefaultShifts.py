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
            Shift.SUNDAY,
            Shift.SATURDAY
        ]

        for day in DAYS:
            Shift.objects.create(
                owner=stylist,
                title="Unavailable",
                dow="[" + str(day) + "]",
                color="red",
                start_time="0:00:00",
                end_time="23:59:00"
            )

        WEEKDAYS = [
            Shift.MONDAY,
            Shift.TUESDAY,
            Shift.WEDNESDAY,
            Shift.THURSDAY,
            Shift.FRIDAY
        ]

        for day in WEEKDAYS:
            Shift.objects.create(
                owner=stylist,
                title="Unavailable",
                dow="[" + str(day) + "]",
                color="red",
                start_time="0:00:00",
                end_time="7:59:00",
            )
            Shift.objects.create(
                owner=stylist,
                title="Unavailable",
                dow="[" + str(day) + "]",
                color="red",
                start_time="18:00:00",
                end_time="23:59:00",
            )
