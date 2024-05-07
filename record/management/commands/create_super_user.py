from decouple import config
from django.core.management.base import BaseCommand

from record.models import CustomUser

USERNAME = config("ADMIN_USERNAME")
PASSWORD = config("ADMIN_PASSWORD")


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(username=USERNAME).exists():
            CustomUser.objects.create_superuser(
                username=USERNAME,
                email=USERNAME,
                password=PASSWORD,
            )
        print("Superuser has been created.")
