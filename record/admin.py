from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from .forms import CustomUserCreationForm, CutomUserChangeForm
from .models import CompetitionData, CustomUser, TrainingData
from .resources import CompetitionDataResource, TrainingDataResource


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CutomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_active",
                "groups",
                "user_permissions",
            ),
        },
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(CompetitionData)
class CompetitionDataAdmin(ImportExportModelAdmin):
    resource_classes = [CompetitionDataResource]


@admin.register(TrainingData)
class TrainingDataAdmin(ImportExportModelAdmin):
    resource_classes = [TrainingDataResource]
