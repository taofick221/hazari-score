from django import forms

from .constants import ROUND_TOTAL
from .models import Game, Round


INPUT_CLASS = (
    "form-control form-control-lg text-center score-input"
)


class GameForm(forms.ModelForm):
    class Meta:
        model = Game

        fields = (
            "target_score",
            "player1_name",
            "player2_name",
            "player3_name",
            "player4_name",
        )

        widgets = {
            "target_score": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "1000",
                    "min": 100,
                    "step": 100,
                }
            ),
            "player1_name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Player 1",
                }
            ),
            "player2_name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Player 2",
                }
            ),
            "player3_name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Player 3",
                }
            ),
            "player4_name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Player 4",
                }
            ),
        }


class RoundForm(forms.ModelForm):
    class Meta:
        model = Round

        fields = (
            "player1_score",
            "player2_score",
            "player3_score",
            "player4_score",
        )

        widgets = {
            "player1_score": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "0",
                    "min": 0,
                }
            ),
            "player2_score": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "0",
                    "min": 0,
                }
            ),
            "player3_score": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "0",
                    "min": 0,
                }
            ),
            "player4_score": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASS,
                    "placeholder": "0",
                    "min": 0,
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        scores = [
            cleaned_data.get("player1_score") or 0,
            cleaned_data.get("player2_score") or 0,
            cleaned_data.get("player3_score") or 0,
            cleaned_data.get("player4_score") or 0,
        ]

        for score in scores:
            if score < 0:
                raise forms.ValidationError(
                    "Score cannot be negative."
                )

        total = sum(scores)

        if total != ROUND_TOTAL:
            raise forms.ValidationError(
                f"Every round total must be exactly {ROUND_TOTAL} points."
            )

        return cleaned_data