from django.http import Http404
from django.shortcuts import render, get_object_or_404

from marathon.models import Event


def active_event(request):
    event = Event.objects.first()
    if event:
        context = {'event': event}
        return render(request, 'marathon/event/details.html', context)
    else:
        raise Http404('No events available')


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    context = {'event': event}
    return render(request, 'marathon/event/details.html', context)