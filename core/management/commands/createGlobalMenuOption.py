from django.core.management import BaseCommand

from core.models import Menu
from core.utils.global_constants import DEFAULT_MENU_PICTURE


class Command(BaseCommand):
    help = "Create Global Menu Option."

    def handle(self, *args, **options):
        Menu.objects.create(
            creator=Menu.ADMIN,
            name='GLOBAL_OPTION',
            picture=DEFAULT_MENU_PICTURE,
            description='Created by a management command.'
        )