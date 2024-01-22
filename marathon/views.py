from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

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

        player = None
        if request.user.is_authenticated:
            player, created = Player.objects.get_or_create(user=request.user)
        player_form = PlayerForm(request.POST, prefix='player', instance=player)

        form = SubmissionForm(request.POST)

        if form.is_valid() and player_form.is_valid():
            submission = form.save(commit=False)
            submission.event = event
            submission.save()

            player = player_form.save()
            submission.players.add(player)

            request.session['previous_form'] = None
            messages.add_message(request, messages.SUCCESS, _('Ilmoittautuminen onnistui!'))
        else:
            request.session['previous_form'] = request.POST
            messages.add_message(request, messages.ERROR, _('Ilmoittautuminen epäonnistui, tarkista lomake.'))
        return HttpResponseRedirect(request.GET.get('next', '/'))
    raise Http404('Tämmöstä ei oo')

def thanks(request):
    return