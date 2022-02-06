from django import forms

from .models import Submission, Player


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = [
            'event',
            'players',
            'hidden'
        ]

PlayerFormSet = forms.inlineformset_factory(Submission, Submission.players.through, fields='__all__')