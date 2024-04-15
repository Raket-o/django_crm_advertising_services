from django.contrib.auth.models import Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create Permissions")

        permission_list = (
            ("to_active_client", 9),
        )

        for permission, content_id in permission_list:
            permission, created = Permission.objects.get_or_create(name=permission, content_type_id=content_id,
                                                                   codename=permission.lower())
            self.stdout.write(f"Created permission {permission.name}")

        self.stdout.write(self.style.SUCCESS("Permissions created"))
