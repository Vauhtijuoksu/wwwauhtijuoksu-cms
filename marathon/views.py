import datetime

from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from .models import Event, Player, Submission
from .forms import SubmissionForm, PlayerForm
from .utils import get_player_info_for_user


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



def edit_submission(request, event, submission_id):
    if request.user.is_authenticated:
        player = get_player_info_for_user(request.user)
    else:
        return HttpResponseRedirect('/')
    event = get_object_or_404(Event, slug=event)
    submission = get_object_or_404(Submission, id=submission_id, event=event, hidden=False, players__in=[player['id']])

    if request.method == 'POST':
        form = SubmissionForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            submission.game_title = form.game_title
            submission.publish_year = form.publish_year
            submission.console = form.console
            submission.console_display = form.console_display
            submission.category = form.category
            submission.estimate = form.estimate
            submission.personal_best = form.personal_best
            submission.time_constraints = form.time_constraints
            submission.description = form.description
            submission.priority = form.priority
            submission.save()
            request.session['previous_form'] = None
            messages.add_message(request, messages.SUCCESS, _('Ilmoittautuminen onnistui!'))
        else:
            request.session['previous_form'] = request.POST
            messages.add_message(request, messages.ERROR, _('Ilmoittautuminen epäonnistui, tarkista lomake.'))
        return HttpResponseRedirect(request.GET.get('next', '/'))

    if request.method == 'GET':

        form = SubmissionForm(initial=vars(submission))
        event_duration = (event.end - event.start).days
        event_days = []
        for d in range(event_duration + 1):
            event_days.append(event.start + datetime.timedelta(days=d))

        context = {
            'event': event,
            'event_days': event_days,
            'require_authentication': True,
            'form': form,
            'submission_id': submission_id,
        }
        return render(request, 'marathon/edit_submission.html', context)
    raise Http404('Tämmöstä ei oo')

def thanks(request):
    return
