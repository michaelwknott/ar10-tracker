from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CompetitionDataForm, TrainingDataForm
from .models import CompetitionData, TrainingData


@login_required
def dashboard(request):
    # Competition data
    competition_data = CompetitionData.objects.all()

    # get personal best score from competition data
    comp_pb = CompetitionData.objects.aggregate(Max("qual_score"))

    # get average of top 3 scores from competition data
    comp_top3 = CompetitionData.objects.order_by("qual_score")[:3]
    comp_top3_avg = comp_top3.aggregate(Avg("qual_score"))

    # get individual dates and scores from competition data queryset
    comp_dates = []
    qual_scores = []

    for competition in competition_data:
        comp_date = competition.date.strftime("%Y.%m.%d")
        qual_score = competition.qual_score

        comp_dates.append(comp_date)
        qual_scores.append(qual_score)

    # Training data
    training_data = TrainingData.objects.all()

    # get personal best score from training data
    training_pb = TrainingData.objects.aggregate(Max("score"))

    # get average of top 3 scores from training data
    training_top3 = TrainingData.objects.order_by("score")[:3]
    training_top3_avg = training_top3.aggregate(Avg("score"))

    # get average of all training data fileds
    training_data_avgs = TrainingData.objects.aggregate(
        Avg("ten_zero"),
        Avg("ten_azero"),
        Avg("ten_five"),
        Avg("ten_afive"),
        Avg("aiming_time"),
        Avg("s1"),
        Avg("s2"),
        Avg("da"),
    )

    # get individual metrics from training data queryset
    training_dates = []
    training_scores = []
    ten_zeros = []
    ten_azeros = []
    ten_fives = []
    ten_afives = []

    for training in training_data:
        training_date = training.date.strftime("%Y.%m.%d")
        training_score = training.score
        ten_five = training.ten_five
        ten_afive = training.ten_afive
        ten_zero = training.ten_zero
        ten_azero = training.ten_azero

        training_dates.append(training_date)
        training_scores.append(training_score)
        ten_zeros.append(ten_zero)
        ten_azeros.append(ten_azero)
        ten_fives.append(ten_five)
        ten_afives.append(ten_afive)

    context = {
        "training_data_avgs": training_data_avgs,
        "comp_dates": comp_dates,
        "qual_scores": qual_scores,
        "training_dates": training_dates,
        "training_scores": training_scores,
        "ten_azeros": ten_azeros,
        "ten_zeros": ten_zeros,
        "ten_afives": ten_afives,
        "ten_fives": ten_fives,
        "comp_top3_avg": comp_top3_avg,
        "comp_pb": comp_pb,
        "training_top3_avg": training_top3_avg,
        "training_pb": training_pb,
    }
    return render(request, "dashboard.html", context=context)


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
        messages.success(request, "Deleted competition data")
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

    if request.method == "POST":
        competition_data.delete()
        messages.success(request, "Deleted competition data")
        return redirect("record:competition_data_list")

    return render(
        request,
        "competition/competition_data_delete.html",
        {"competition_data": competition_data},
    )
