from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Event, Player, Submission
from .forms import SubmissionForm


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
    form = SubmissionForm()

    context = {
        'form': form,
    }

    return render(request, 'marathon/submission_form.html', context)
