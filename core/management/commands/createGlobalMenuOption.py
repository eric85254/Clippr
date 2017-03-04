from django.core.management import BaseCommand

from core.models import GlobalMenu
from core.utils.global_constants import DEFAULT_MENU_PICTURE


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