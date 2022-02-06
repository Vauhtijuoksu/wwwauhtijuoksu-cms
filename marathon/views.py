from django.http import Http404
from django.shortcuts import render, get_object_or_404

from marathon.models import Event
from .forms import SubmissionForm, PlayerFormSet


def active_event(request):
    event = Event.objects.first()
    if event:
        context = {'event': event}
        return render(request, 'marathon/event/details.html', context)
    else:
        raise Http404('No events available')


def event_detail(request, event):
    event = get_object_or_404(Event, slug=event)
    context = {'event': event}
    return render(request, 'marathon/event/details.html', context)


def new_submission(request, event):
    event = get_object_or_404(Event, slug=event)
    form = SubmissionForm()
    formset = PlayerFormSet()

    context = {
        'form': form,
        'player_formset': formset
    }

    return render(request, 'marathon/event/submission_form.html', context)


def edit_submission(request, pk):
    pass