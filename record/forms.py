from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CutomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
