from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GameForm, RoundForm
from .models import Game, Round
from .services import (
    get_dashboard_data,
    get_next_round_number,
    get_rounds,
)


def home(request):
    if request.method == "POST":
        form = GameForm(request.POST)

        if form.is_valid():
            game = form.save()

            messages.success(
                request,
                "🎮 New Hazari game created successfully!",
            )

            return redirect(
                "game:game_detail",
                pk=game.pk,
            )

    else:
        form = GameForm()

    return render(
        request,
        "game/home.html",
        {
            "form": form,
        },
    )


def game_detail(request, pk):
    game = get_object_or_404(
        Game,
        pk=pk,
    )

    if request.method == "POST":

        form = RoundForm(request.POST)

        if form.is_valid():

            round_obj = form.save(commit=False)

            round_obj.game = game

            round_obj.round_number = (
                get_next_round_number(game)
            )

            round_obj.save()

            messages.success(
                request,
                "🎉 Round saved successfully!",
            )

            return redirect(
                "game:game_detail",
                pk=game.pk,
            )

    else:

        form = RoundForm()

    context = {
        "game": game,
        "form": form,
        "rounds": get_rounds(game),
    }

    context.update(
        get_dashboard_data(game)
    )

    return render(
        request,
        "game/game.html",
        context,
    )


def history(request, pk):
    game = get_object_or_404(
        Game,
        pk=pk,
    )

    return render(
        request,
        "game/history.html",
        {
            "game": game,
            "rounds": get_rounds(game),
        },
    )


def edit_round(request, pk):

    round_obj = get_object_or_404(
        Round,
        pk=pk,
    )

    if request.method == "POST":

        form = RoundForm(
            request.POST,
            instance=round_obj,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "✏️ Round updated successfully!",
            )

            return redirect(
                "game:game_detail",
                pk=round_obj.game.pk,
            )

    else:

        form = RoundForm(
            instance=round_obj,
        )

    return render(
        request,
        "game/edit_round.html",
        {
            "game": round_obj.game,
            "round": round_obj,
            "form": form,
        },
    )


def delete_round(request, pk):

    round_obj = get_object_or_404(
        Round,
        pk=pk,
    )

    game = round_obj.game

    if request.method == "POST":

        round_obj.delete()

        messages.warning(
            request,
            "🗑️ Round deleted successfully!",
        )

    return redirect(
        "game:game_detail",
        pk=game.pk,
    )


def reset_game(request, pk):

    game = get_object_or_404(
        Game,
        pk=pk,
    )

    if request.method == "POST":

        game.rounds.all().delete()

        messages.error(
            request,
            "🔄 Game reset successfully!",
        )

    return redirect(
        "game:game_detail",
        pk=game.pk,
    )