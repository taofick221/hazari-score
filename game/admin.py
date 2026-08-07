from django.contrib import admin

from .models import Game, Round


class RoundInline(admin.TabularInline):
    model = Round
    extra = 0
    ordering = ("-round_number",)

    fields = (
        "round_number",
        "player1_score",
        "player2_score",
        "player3_score",
        "player4_score",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "target_score",
        "player1_name",
        "player2_name",
        "player3_name",
        "player4_name",
        "is_finished",
        "created_at",
    )

    list_filter = (
        "is_finished",
        "created_at",
    )

    search_fields = (
        "player1_name",
        "player2_name",
        "player3_name",
        "player4_name",
    )

    ordering = (
        "-created_at",
    )

    inlines = [
        RoundInline,
    ]


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):

    list_display = (
        "game",
        "round_number",
        "player1_score",
        "player2_score",
        "player3_score",
        "player4_score",
        "total_score",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    search_fields = (
        "game__player1_name",
        "game__player2_name",
        "game__player3_name",
        "game__player4_name",
    )