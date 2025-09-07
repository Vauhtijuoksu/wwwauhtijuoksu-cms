import re

from django import forms
from django.forms import formset_factory
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from pkg_resources import require


from .models import Submission, Player

TEXTAREA_ATTRS = {'rows': 2, 'cols': 30}

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['user']
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': 'Nimimerkki pelaajalistaukseen'}),
            'discord': forms.TextInput(attrs={'placeholder': 'Nick'}),
            'gmail': forms.TextInput(attrs={'placeholder': 'etu.suku@gmail.com'}),
            'twitch': forms.TextInput(attrs={'placeholder': 'nimi_merkki'}),
        }


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = [
            'event',
            'players',
            'hidden',
            'video_link'
            'scoreboard_link',
            'for_children',
            'flashing_lights'
        ]
        widgets = {
            'game_title': forms.TextInput(attrs={'placeholder': 'Sakarin Villapaitapeli'}),
            'publish_year': forms.NumberInput(attrs={'placeholder': '1969'}),
            'console': forms.TextInput(attrs={'placeholder': 'PC'}),
            'console_display': forms.TextInput(attrs={'placeholder': 'NES'}),
            'category': forms.TextInput(attrs={'placeholder': 'Any% NMS'}),
            'estimate': forms.TextInput(attrs={'placeholderHours': '1','placeholderMinutes': '30'}),
            'personal_best': forms.TextInput(attrs={'placeholderHours': '1','placeholderMinutes': '19'}),
            'time_constraints': forms.Textarea(attrs=TEXTAREA_ATTRS),
            'description': forms.Textarea(attrs=TEXTAREA_ATTRS),
            'priority': forms.NumberInput(attrs={'min': '1'}),
            'gdpr': forms.CheckboxInput(attrs={'required': True, 'pre_label': 'Tietosuoja'})
        }
