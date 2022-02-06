from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Event, Player, Submission
from .forms import SubmissionForm, PlayerFormSet


def active_event(request):
    event = Event.objects.first()
    if event:
        context = {'event': event}
        return render(request, 'marathon/event_details.html', context)
    else:
        raise Http404('No events available')


def event_detail(request, event):
    event = get_object_or_404(Event, slug=event)
    context = {'event': event}
    return render(request, 'marathon/event_details.html', context)


def new_submission(request, event):
    event = get_object_or_404(Event, slug=event)
    if request.method == 'POST':
        players_formset = PlayerFormSet(request.POST)
        form = SubmissionForm(request.POST)
        # TODO: Save submission
        if form.is_valid():
            # TODO: Show success message
            pass
        else:
            # TODO: Show error message
            pass
        return HttpResponseRedirect(request.GET.get('next', '/'))
    raise Http404('Tämmöstä ei oo')

def thanks(request):
    return