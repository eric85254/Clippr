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
            phone_number="0000000001",
            is_stylist="YES"
        )

        customer = User(
            first_name="I am a",
            last_name="customer",
            email="customer@gmail.com",
            phone_number="0000000002",
            is_stylist="NO"
        )

        superuser = User(
            first_name="I am a",
            last_name="superuser",
            email="development@clippr.org",
            phone_number="0000000003",
            is_stylist="NO",
            is_staff=True,
            is_superuser=True
        )

        stylist.set_password(password)
        customer.set_password(password)
        superuser.set_password(password)

        stylist.save()
        customer.save()
        superuser.save()