"""
    This module creates two Global Menu Options for Stylists to choose from.
    The two options are "Girl's Haircut" and "Boy's Haircut" for $50.00 each.
"""
import datetime

from django.core.management import BaseCommand

from core.models import GlobalMenu


class Command(BaseCommand):
    help = "Create Global Menu Option."

    def handle(self, *args, **options):
        GlobalMenu.objects.create(
            name="Short Cut",
            price=20.00,
            duration=datetime.timedelta(hours=1.0)
        )
        GlobalMenu.objects.create(
            name="Medium Cut",
            price=30.00,
            duration=datetime.timedelta(hours=1.5)
        )
        GlobalMenu.objects.create(
            name="Long Cut",
            price=40.00,
            duration=datetime.timedelta(hours=2.0)
        )