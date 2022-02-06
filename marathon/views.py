from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Event, Player, Submission
from .forms import SubmissionForm, PlayerForm


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
    if request.method == 'POST':
        event = get_object_or_404(Event, slug=event)
        player_form = PlayerForm(request.POST, prefix='player')
        form = SubmissionForm(request.POST, )

        if form.is_valid() and player_form.is_valid():
            submission = form.save(commit=False)
            submission.event = event
            submission.save()

            player = player_form.save()
            submission.players.add(player)
            # TODO: Show success message
        else:
            # TODO: Show error message
            pass
        return HttpResponseRedirect(request.GET.get('next', '/'))
    raise Http404('Tämmöstä ei oo')

def thanks(request):
    return