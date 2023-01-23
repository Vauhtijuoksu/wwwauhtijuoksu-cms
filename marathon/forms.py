import re

from django import forms
from django.forms import formset_factory
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import Submission, Player

TEXTAREA_ATTRS = {'rows': 2, 'cols': 30}

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ['user']
        widgets = {
            'allergies': forms.Textarea(attrs=TEXTAREA_ATTRS)
        }


estimate_validator = RegexValidator(
    regex=r'^\d{1,2}:[0-5][05]$',
    message=_('aika-arvio muodossa hh:mm, viiden minuutin tarkkuudella.')
)

class SubmissionForm(forms.ModelForm):
    gdpr = forms.BooleanField(required=True, label=_('Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti'))

    def clean_estimate(self):

        estimate = self.cleaned_data['estimate']
        ptr = re.fullmatch(r'(?P<hours>[0-9]{1,2}):(?P<minutes>[0-5][0-9])', estimate)

        if not ptr:
            raise ValidationError(_('aika-arvio muodossa hh:mm'))

        hours = int(ptr.group('hours'))

        if hours > 16:
            raise ValidationError(_('liian pitkä runi :/ kokeile jotain lyhempää!'))

        minutes = int(ptr.group('minutes'))
        total = hours * 60 + minutes
        total_rounded = total + (5 - total) % 5

        cleaned_hours = total_rounded // 60
        cleaned_minutes = total_rounded % 60
        cleaned_estimate = f'{cleaned_hours:02}:{cleaned_minutes:02}'

        return cleaned_estimate

    class Meta:
        model = Submission
        exclude = [
            'event',
            'players',
            'hidden',
            'scoreboard_link',
            'for_children',
            'flashing_lights'
        ]
        widgets = {
            'time_constraints': forms.Textarea(attrs=TEXTAREA_ATTRS),
            'description': forms.Textarea(attrs=TEXTAREA_ATTRS),
        }
