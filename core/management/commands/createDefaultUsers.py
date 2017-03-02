from optparse import make_option

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'My custom django management command'

    def handle(self, *args, **options):
        from core.models import User

        password = "clippr"

        stylist = User(
            first_name="I am a",
            last_name="stylist",
            email="stylist@gmail.com",
            phone_number="4804151890",
            is_stylist="YES"
        )

        customer = User(
            first_name="I am a",
            last_name="customer",
            email="customer@gmail.com",
            phone_number="4807202341",
            is_stylist="NO"
        )

        stylist.set_password(password)
        customer.set_password(password)

        stylist.save()
        customer.save()