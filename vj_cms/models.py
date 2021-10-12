from cms.models import CMSPlugin
from django.db import models


class GameInfo(models.Model):
    api_id = models.UUIDField(unique=True)
    game = models.TextField()
    device = models.TextField()
    player = models.TextField()
    player_twitch = models.TextField()
    published = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    vod_link = models.TextField()


class GameInfoPlugin(CMSPlugin):
    game = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
