from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CompetitionDataForm, TrainingDataForm
from .models import CompetitionData, TrainingData


@login_required
def training_data_list(request):
    training_data = TrainingData.objects.all()
    training_data = training_data.filter(user=request.user)
    context = {"training_data": training_data}

    return render(request, "training/training_data_list.html", context)


@login_required
def training_data_new(request):
    if request.method == "POST":
        form = TrainingDataForm(request.POST)
        if form.is_valid():
            training_data = form.save(commit=False)
            training_data.user = request.user
            training_data.save()
            messages.success(request, "Added training data")

            return redirect("record:training_data_list")
    else:
        form = TrainingDataForm()

    return render(request, "training/training_data.html", {"form": form})


@login_required
def training_data_edit(request, pk):
    training_data = get_object_or_404(TrainingData, pk=pk, user=request.user)

    if request.method == "POST":
        form = TrainingDataForm(request.POST, instance=training_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated training data")

            return redirect("record:training_data_list")
    else:
        form = TrainingDataForm(instance=training_data)

    return render(
        request,
        "training/training_data_edit.html",
        {"training_data": training_data, "form": form},
    )


@login_required
def training_data_delete(request, pk):
    training_data = get_object_or_404(TrainingData, pk=pk, user=request.user)
    training_data.delete()
    messages.success(request, "Deleted training data")

    return HttpResponse(status=200)


@login_required
def competition_data_list(request):
    competition_data = CompetitionData.objects.all()
    competition_data = competition_data.filter(user=request.user)

    context = {"competition_data": competition_data}

    return render(request, "competition/competition_data_list.html", context)


@login_required
def competition_data_new(request):
    if request.method == "POST":
        form = CompetitionDataForm(request.POST)
        if form.is_valid():
            competition_data = form.save(commit=False)
            competition_data.user = request.user
            competition_data.save()

            messages.success(request, "Added competition data")

            return redirect("record:competition_data_list")
    else:
        form = CompetitionDataForm()

    return render(request, "competition/competition.html", {"form": form})


@login_required
def competition_data_edit(request, pk):
    competition_data = get_object_or_404(CompetitionData, pk=pk, user=request.user)
    if request.method == "POST":
        form = CompetitionDataForm(request.POST, instance=competition_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated competition data")

            return redirect("record:competition_data_list")
    else:
        form = CompetitionDataForm(instance=competition_data)

    return render(
        request,
        "competition/competition_data_edit.html",
        {"competition_data": competition_data, "form": form},
    )


@login_required
def competition_data_delete(request, pk):
    competition_data = get_object_or_404(CompetitionData, pk=pk, user=request.user)
    competition_data.delete()
    messages.success(request, "Deleted competition data")

    return HttpResponse(status=200)
