from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Max
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CompetitionDataForm, TrainingDataForm
from .models import CompetitionData, TrainingData


@login_required
def dashboard(request):
    # Competition data
    competition_data = CompetitionData.objects.all()

    # Get personal best score from competition data
    comp_pb = competition_data.aggregate(Max("qual_score"))

    # Get average of top 3 scores from competition data
    comp_top3_avg = competition_data.order_by("-qual_score")[:3].aggregate(
        Avg("qual_score")
    )

    # Training data
    training_data = TrainingData.objects.all()

    # Get personal best score from training data
    training_pb = training_data.aggregate(Max("score"))

    # Get average of top 3 scores from training data
    training_top3_avg = training_data.order_by("-score")[:3].aggregate(Avg("score"))

    # Get average of all training data fields
    training_data_avgs = training_data.aggregate(
        Avg("ten_zero"),
        Avg("ten_azero"),
        Avg("ten_five"),
        Avg("ten_afive"),
        Avg("aiming_time"),
        Avg("s1"),
        Avg("s2"),
        Avg("da"),
    )

    context = {
        "competition_data": competition_data,
        "training_data": training_data,
        "comp_top3_avg": comp_top3_avg,
        "comp_pb": comp_pb,
        "training_top3_avg": training_top3_avg,
        "training_pb": training_pb,
        "training_data_avgs": training_data_avgs,
    }
    return render(request, "dashboard.html", context=context)


@login_required
def training_data_list(request):
    training_data = TrainingData.objects.all()
    training_data = training_data.filter(user=request.user)
    paginator = Paginator(training_data, 20)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {"training_data_page_obj": page_object}

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

    return render(request, "training/training.html", {"form": form})


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

    if request.method == "POST":
        training_data.delete()
        messages.error(request, "Deleted competition data")
        return redirect("record:training_data_list")

    return render(
        request,
        "training/training_data_delete.html",
        {"training_data": training_data},
    )


@login_required
def competition_data_list(request):
    competition_data = CompetitionData.objects.all()
    competition_data = competition_data.filter(user=request.user)
    paginator = Paginator(competition_data, 20)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {"competition_data_page_obj": page_object}

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

    if request.method == "POST":
        competition_data.delete()
        messages.error(request, "Deleted competition data")
        return redirect("record:competition_data_list")

    return render(
        request,
        "competition/competition_data_delete.html",
        {"competition_data": competition_data},
    )
