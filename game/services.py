from django.db.models import Max, Sum

from .constants import ROUND_TOTAL
from .utils import (
    get_game_banner,
    get_rank_messages,
    get_winner_popup,
    leaderboard_cards,
)


def get_rounds(game):
    return game.rounds.order_by("-round_number")


def get_next_round_number(game):
    last = game.rounds.aggregate(
        number=Max("round_number")
    )["number"]

    if last is None:
        return 1

    return last + 1


def calculate_totals(game):
    totals = game.rounds.aggregate(
        player1=Sum("player1_score"),
        player2=Sum("player2_score"),
        player3=Sum("player3_score"),
        player4=Sum("player4_score"),
    )

    return {
        "player1": totals["player1"] or 0,
        "player2": totals["player2"] or 0,
        "player3": totals["player3"] or 0,
        "player4": totals["player4"] or 0,
    }


def calculate_remaining(game):
    totals = calculate_totals(game)

    return {
        "player1": max(game.target_score - totals["player1"], 0),
        "player2": max(game.target_score - totals["player2"], 0),
        "player3": max(game.target_score - totals["player3"], 0),
        "player4": max(game.target_score - totals["player4"], 0),
    }


def get_leaderboard(game):
    totals = calculate_totals(game)
    remaining = calculate_remaining(game)

    leaderboard = [
        {
            "name": game.player1_name,
            "score": totals["player1"],
            "remaining": remaining["player1"],
        },
        {
            "name": game.player2_name,
            "score": totals["player2"],
            "remaining": remaining["player2"],
        },
        {
            "name": game.player3_name,
            "score": totals["player3"],
            "remaining": remaining["player3"],
        },
        {
            "name": game.player4_name,
            "score": totals["player4"],
            "remaining": remaining["player4"],
        },
    ]

    leaderboard.sort(
        key=lambda player: player["score"],
        reverse=True,
    )

    return leaderboard


def get_leaderboard_cards(game):
    leaderboard = get_leaderboard(game)

    return leaderboard_cards(
        leaderboard,
        game.target_score,
    )


def check_winner(game):
    leaderboard = get_leaderboard(game)

    if not leaderboard:
        return None

    first = leaderboard[0]

    if first["score"] >= game.target_score:
        return first

    return None


def get_statistics(game):
    rounds = game.rounds.count()

    totals = calculate_totals(game)

    highest = max(totals.values())

    return {
        "target": game.target_score,
        "round_total": ROUND_TOTAL,
        "total_rounds": rounds,
        "highest_score": highest,
    }


def get_dashboard_data(game):
    winner = check_winner(game)

    return {
        "leaderboard": get_leaderboard(game),
        "leaderboard_cards": get_leaderboard_cards(game),
        "totals": calculate_totals(game),
        "remaining": calculate_remaining(game),
        "statistics": get_statistics(game),
        "winner": winner,
        "winner_message": get_winner_popup() if winner else None,
        "game_banner": get_game_banner(),
        "rank_messages": get_rank_messages(),
    }