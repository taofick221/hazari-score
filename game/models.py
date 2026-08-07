from django.core.validators import MinValueValidator
from django.db import models

from .constants import ROUND_TOTAL


class Game(models.Model):
    target_score = models.PositiveIntegerField(
        default=1000
    )

    player1_name = models.CharField(max_length=50)
    player2_name = models.CharField(max_length=50)
    player3_name = models.CharField(max_length=50)
    player4_name = models.CharField(max_length=50)

    is_finished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.player1_name} vs "
            f"{self.player2_name} vs "
            f"{self.player3_name} vs "
            f"{self.player4_name}"
        )


class Round(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="rounds",
    )

    round_number = models.PositiveIntegerField()

    player1_score = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    player2_score = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    player3_score = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    player4_score = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-round_number"]
        unique_together = ("game", "round_number")

    def __str__(self):
        return (
            f"Round {self.round_number}"
        )

    @property
    def total_score(self):
        return (
            self.player1_score
            + self.player2_score
            + self.player3_score
            + self.player4_score
        )

    @property
    def is_valid(self):
        return self.total_score == ROUND_TOTAL