from django.urls import path

from . import views

app_name = "game"

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "game/<int:pk>/",
        views.game_detail,
        name="game_detail",
    ),

    path(
        "game/<int:pk>/history/",
        views.history,
        name="history",
    ),

    path(
        "round/<int:pk>/edit/",
        views.edit_round,
        name="edit_round",
    ),

    path(
        "round/<int:pk>/delete/",
        views.delete_round,
        name="delete_round",
    ),

    path(
        "game/<int:pk>/reset/",
        views.reset_game,
        name="reset_game",
    ),
]