from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm

from .models import CompetitionData, CustomUser, TrainingData


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CutomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class TrainingDataForm(ModelForm):
    class Meta:
        model = TrainingData
        exclude = ("user",)
        fields = "__all__"


class CompetitionDataForm(ModelForm):
    class Meta:
        model = CompetitionData
        exclude = ("user",)
        fields = "__all__"
