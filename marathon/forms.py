from django import forms
from django.forms import modelformset_factory

from .models import Submission, Player



class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = [
            'event',
            'players',
            'hidden'
        ]

PlayerFormSet = modelformset_factory(Player, exclude=('user',))