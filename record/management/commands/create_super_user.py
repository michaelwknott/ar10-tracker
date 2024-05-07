from decouple import config
from django.core.management.base import BaseCommand

from record.models import CustomUser

EMAIL = config("ADMIN_EMAIL")
PASSWORD = config("ADMIN_PASSWORD")


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email=EMAIL).exists():
            CustomUser.objects.create_superuser(
                email=EMAIL,
                password=PASSWORD,
            )
        print("Superuser has been created.")
