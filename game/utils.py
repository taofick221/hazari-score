from .constants import (
    ROUND_TOTAL,
    random_game_banner,
    random_king_message,
    random_last_message,
    random_second_message,
    random_third_message,
    random_winner_message,
)


def calculate_auto_score(scores, auto_index):
    """
    scores = [120, 50, 0, 0]
    auto_index = 3

    return 190
    """

    total = 0

    for index, score in enumerate(scores):
        if index != auto_index:
            total += score or 0

    remaining = ROUND_TOTAL - total

    return max(remaining, 0)


def validate_round(scores):
    """
    Return True if total == ROUND_TOTAL.
    """

    total = sum(score or 0 for score in scores)

    return total == ROUND_TOTAL


def calculate_progress(score, target):
    """
    Return progress percentage.
    """

    if target <= 0:
        return 0

    percentage = (score / target) * 100

    return min(round(percentage), 100)


def get_rank_messages():
    """
    Random funny messages for leaderboard.
    """

    return {
        1: random_king_message(),
        2: random_second_message(),
        3: random_third_message(),
        4: random_last_message(),
    }


def get_game_banner():
    """
    Funny banner shown when game starts.
    """

    return random_game_banner()


def get_winner_popup():
    """
    Funny winner popup message.
    """

    return random_winner_message()


def leaderboard_cards(leaderboard, target):
    """
    leaderboard = [
        {
            "name": "...",
            "score": ...
        }
    ]
    """

    messages = get_rank_messages()

    cards = []

    for position, player in enumerate(leaderboard, start=1):

        cards.append(
            {
                "position": position,
                "name": player["name"],
                "score": player["score"],
                "remaining": player["remaining"],
                "progress": calculate_progress(
                    player["score"],
                    target,
                ),
                "message": messages[position],
            }
        )

    return cards