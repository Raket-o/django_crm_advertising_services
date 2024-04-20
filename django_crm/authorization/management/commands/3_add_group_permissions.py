from django.contrib.auth.models import Group
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        groups = Group.objects.all()
        if not groups:
            self.stdout.write("no groups found")
            return

        groups[0].permissions.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16,)
        groups[1].permissions.add(33, 34, 35, 36,)
        groups[2].permissions.add(25, 26, 27, 28, 29, 30, 31, 32,)
        groups[3].permissions.add(37, 38, 39, 40, 36, 41, 42, 43, 44)
        self.stdout.write(self.style.SUCCESS("Add group permissions"))
