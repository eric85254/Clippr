"""
    Creates dummy portfolio items for the dummy stylist account.
"""
import datetime

from django.core.management import BaseCommand

from core.models import User
from core.utils.global_constants import DEFAULT_HAIRCUT_1, DEFAULT_HAIRCUT_2, DEFAULT_HAIRCUT_3
from stylist.models import PortfolioHaircut


class Command(BaseCommand):
    help = "Create Default Haircuts... You need to create default stylists first!"

    def handle(self, *args, **options):
        stylist = User.objects.get(email='stylist@gmail.com')
        PortfolioHaircut.objects.create(
            stylist=stylist,
            picture=DEFAULT_HAIRCUT_1,
            name="Default Haircut One",
            description="Bitch ass haircut one.",
            price=15.00,
            duration=datetime.timedelta(hours=1)
        )
        PortfolioHaircut.objects.create(
            stylist=stylist,
            picture=DEFAULT_HAIRCUT_2,
            name="Default Haircut Two",
            description="Bitch ass haircut Two.",
            price=15.00,
            duration=datetime.timedelta(hours=1)
        )
        PortfolioHaircut.objects.create(
            stylist=stylist,
            picture=DEFAULT_HAIRCUT_3,
            name="Default Haircut Three",
            description="Bitch ass haircut Three.",
            price=15.00,
            duration=datetime.timedelta(hours=1)
        )