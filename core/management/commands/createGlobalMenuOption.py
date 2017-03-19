"""
    This module creates two Global Menu Options for Stylists to choose from.
    The two options are "Girl's Haircut" and "Boy's Haircut" for $50.00 each.
"""
from django.core.management import BaseCommand

from core.models import GlobalMenu


class Command(BaseCommand):
    help = "Create Global Menu Option."

    def handle(self, *args, **options):
        GlobalMenu.objects.create(
            name="Girl's Haircut",
            price=50.00
        )
        GlobalMenu.objects.create(
            name="Boy's Haircut",
            price=20.00
        )