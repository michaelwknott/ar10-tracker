from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


def __str__(self):
    return self.email
