from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from vj_cms.client import VJClient
from vj_cms.models import GameInfo

client = VJClient(settings.VJ_API_URL)

def update_timetable(request):
    games = client.games()
    for game in games:
        api_id = game.pop('id')
        GameInfo.objects.update_or_create(
            api_id=api_id,
            defaults=game
        )

    return HttpResponse('Updated, thanks!')
