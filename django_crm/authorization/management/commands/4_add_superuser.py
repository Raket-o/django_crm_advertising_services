from django.contrib.auth.models import User
from django.core.management import BaseCommand

from env_data import login_superuser


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create superuser")

        superuser, created = User.objects.get_or_create(
            password="pbkdf2_sha256$720000$VPZHdMONCcHSJljzWYws8S$/ounvLrr0Au7AwU23u0XN3ot5+GQnnDjjARhf0Oywts=",
            is_superuser=True,
            username=login_superuser,
            is_staff=True,
            is_active=True
        )
        self.stdout.write(self.style.SUCCESS("Superuser created"))
