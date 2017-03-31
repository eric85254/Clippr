"""
    This module creates three default users for testing purposes.
    | The password is 'clippr' for every user.

    | The three user's are as follows:
    1. Stylist (email = "stylist@gmail.com")
    2. Customer (email = "stylist@gmail.com")
    3. Superuser (email = "development@clippr.org")
"""
from datetime import timedelta

from django.core.management import BaseCommand

from core.models import User, GlobalMenu
from core.utils.dummy_user_information import stylist_information, customer_information
from stylist.utils.dummy_portfoliohaircut_information import DUMMY_PORTFOLIO_PICTURES
from stylist.models import StylistMenu, PortfolioHaircut


class Command(BaseCommand):
    help = 'My custom django management command'

    global_menu_options = GlobalMenu.objects.all()

    def handle(self, *args, **options):

        password = "clippr"

        for user in stylist_information:
            self.create_dummy_stylist(password, user)

        for user in customer_information:
            self.create_dummy_customer(password, user)

        superuser = User(
            first_name="I am a",
            last_name="superuser",
            email="development@clippr.org",
            phone_number="1100000001",
            is_stylist="NO",
            is_staff=True,
            is_superuser=True
        )
        superuser.set_password(password)
        superuser.save()

    '''
        HELPER FUNCTIONS
    '''

    def create_dummy_customer(self, password, user):
        customer = User(
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            email=user.get('email'),
            phone_number="",
            is_stylist="NO"
        )
        customer.set_password(password)
        customer.save()

    def create_dummy_stylist(self, password, user):
        stylist = User(
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            email=user.get('email'),
            phone_number=user.get('phone_number'),
            profile_picture=user.get('profile_picture'),
            is_stylist="YES"
        )
        stylist.set_password(password)
        stylist.save()

        for global_menu in self.global_menu_options:
            StylistMenu.copy_global(StylistMenu(), global_menu, stylist)

        name_key = stylist.first_name.lower() + '_' + stylist.last_name.lower()
        portfolio_haircuts = DUMMY_PORTFOLIO_PICTURES.get(name_key)

        for haircut in portfolio_haircuts:
            PortfolioHaircut.objects.create(
                stylist=stylist,
                picture=haircut.get('picture'),
                name=haircut.get('name'),
                description=haircut.get('description'),
                price=haircut.get('price'),
                duration=timedelta(hours=1),
            )
