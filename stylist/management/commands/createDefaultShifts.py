"""
    Creates a dummy shift schedule for a dummy stylist
"""
from datetime import timedelta, datetime

from django.core.management import BaseCommand

from core.models import User
from stylist.models import Shift, ShiftException


class Command(BaseCommand):
    help = "create dummy shift schedule for stylist@gmail.com... create the dummy account first!"

    def handle(self, *args, **options):
        stylist = User.objects.get(email="stylist@gmail.com")

        DAYS = [
            Shift.SUNDAY,
            Shift.SATURDAY
        ]

        for day in DAYS:
            new_shift = Shift(
                owner=stylist,
                title="Unavailable",
                dow="[" + str(day) + "]",
                color="red",
                start_time="1:00:00",
                end_time="23:59:00",
            )
            new_shift.save()
            self.create_exception(new_shift)

        WEEKDAYS = [
            Shift.MONDAY,
            Shift.TUESDAY,
            Shift.WEDNESDAY,
            Shift.THURSDAY,
            Shift.FRIDAY
        ]

        for day in WEEKDAYS:
            shift1 = Shift(
                owner=stylist,
                title="Unavailable",
                dow="[" + str(day) + "]",
                color="red",
                start_time="1:00:00",
                end_time="7:59:00",
            )
            shift1.save()
            self.create_exception(shift1)

            shift2 = Shift(
                owner=stylist,
                title="Unavailable",
                dow="[" + str(day) + "]",
                color="red",
                start_time="18:00:00",
                end_time="23:59:00",
            )
            shift2.save()
            self.create_exception(shift2)

    def create_exception(self, new_shift):
        start = datetime.date(datetime.strptime('2017-01-01', '%Y-%m-%d'))
        ShiftException.objects.create(
            shift=new_shift,
            start=start,
            end=start + timedelta(weeks=2600)
        )
