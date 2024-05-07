from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

USERNAME = config("ADMIN_USERNAME")
PASSWORD = config("ADMIN_PASSWORD")


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username=USERNAME).exists():
            User.objects.create_superuser(
                username=USERNAME,
                email=USERNAME,
                password=PASSWORD,
            )
        print("Superuser has been created.")
