from django import forms
from django.forms import formset_factory
from django.utils.translation import gettext_lazy as _

from .models import Submission, Player

TEXTAREA_ATTRS = {'rows': 2, 'cols': 30}

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['user']
        widgets = {
            'allergies': forms.Textarea(attrs=TEXTAREA_ATTRS)
        }

class SubmissionForm(forms.ModelForm):
    gdpr = forms.BooleanField(required=True, label=_('Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti'))
    class Meta:
        model = Submission
        exclude = [
            'event',
            'players',
            'hidden',
            'console_display',
        ]
        widgets = {
            'time_constraints': forms.Textarea(attrs=TEXTAREA_ATTRS),
            'description': forms.Textarea(attrs=TEXTAREA_ATTRS),
        }
