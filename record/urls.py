from django.urls import path

from . import views

app_name = "record"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("training/", views.training_data_list, name="training_data_list"),
    path("training/new/", views.training_data_new, name="training_data_new"),
    path(
        "training/<int:pk>/edit/", views.training_data_edit, name="training_data_edit"
    ),
    path(
        "training/<int:pk>/delete/",
        views.training_data_delete,
        name="training_data_delete",
    ),
    path("competition/", views.competition_data_list, name="competition_data_list"),
    path("competition/new", views.competition_data_new, name="competition_data_new"),
    path(
        "competition/<int:pk>/edit/",
        views.competition_data_edit,
        name="competition_data_edit",
    ),
    path(
        "competition/<int:pk>/delete",
        views.competition_data_delete,
        name="competition_data_delete",
    ),
]
