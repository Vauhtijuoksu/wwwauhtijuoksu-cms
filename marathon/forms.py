from django import forms
from django.forms import formset_factory

from .models import Submission, Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['user']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = [
            'event',
            'players',
            'hidden'
        ]
