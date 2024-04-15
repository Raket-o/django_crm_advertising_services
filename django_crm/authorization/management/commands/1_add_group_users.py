from django.contrib.auth.models import Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create groups")

        group_list = (
            "administrator",
            "operator",
            "marketing",
            "manager",
        )

        for group in group_list:
            group, created = Group.objects.get_or_create(name=group)
            self.stdout.write(f"Created group {group.name}")

        self.stdout.write(self.style.SUCCESS("Groups created"))



