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


class CompetitionData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    competition_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    match_number = models.PositiveSmallIntegerField()
    qual_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        date = self.date_time.date()
        return f"{self.user}: {self.competition_name}, {self.match_number}, {date}"

    class Meta:
        verbose_name_plural = "competition data"
        ordering = ["date_time"]


class TrainingData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField()
    number_shots = models.PositiveSmallIntegerField("Number of shots completed")
    score = models.DecimalField(max_digits=5, decimal_places=2)
    target_distance = models.DecimalField(max_digits=10, decimal_places=1)
    f_coefficient = models.PositiveSmallIntegerField("Ballistic 'F' coefficient")
    aiming_time = models.DecimalField("T", max_digits=10, decimal_places=1)
    score_decimal = models.DecimalField("R", max_digits=10, decimal_places=2)
    ten_zero = models.PositiveSmallIntegerField("10.0")
    ten_azero = models.PositiveSmallIntegerField("10a0")
    ten_five = models.PositiveSmallIntegerField("10.5")
    ten_afive = models.PositiveSmallIntegerField("10a5")
    s1 = models.DecimalField("S1", max_digits=10, decimal_places=1)
    s2 = models.DecimalField("S2", max_digits=10, decimal_places=1)
    da = models.DecimalField("DA", max_digits=10, decimal_places=1)

    def __str__(self):
        date = self.date_time.date()
        return f"{self.user}: {self.number_shots} training match completed on {date}"

    class Meta:
        verbose_name_plural = "training data"
        ordering = ["date_time"]
