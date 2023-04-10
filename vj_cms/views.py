from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from vj_cms.client import VJClient
from vj_cms.models import GameInfo, PlayerInfo

client = VJClient(settings.VJ_API_URL)


def update_timetable(request):
    players = client.players()
    PlayerInfo.objects.all().delete()
    for player in players:
        api_id = player.pop('id')
        PlayerInfo.objects.update_or_create(
            api_id=api_id,
            defaults=player
        )
    games = client.games()
    # TODO: Don't delete once api ID's are fixed
    GameInfo.objects.all().delete()
    for game in games:
        api_id = game.pop('id')
        game_players = game.pop('players')
        game_, _ = GameInfo.objects.update_or_create(
            api_id=api_id,
            defaults=game
        )
        for player_id in game_players:
            player = PlayerInfo.objects.get(api_id=player_id)
            game_.players.add(player)


    return HttpResponse('Updated, thanks!')
