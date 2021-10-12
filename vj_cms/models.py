from cms.models import CMSPlugin
from django.db import models


class GameInfo(models.Model):
    # From API
    api_id = models.UUIDField(primary_key=True)
    game = models.TextField('name')
    device = models.TextField('device')
    player = models.TextField('player nick')
    player_twitch = models.TextField('twitch', blank=True)
    published = models.TextField('publishing year', blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True)
    vod_link = models.URLField(blank=True)

    # Custom added fields
    icon = models.ImageField(null=True, blank=True)
    estimate = models.PositiveIntegerField('estimate in seconds')
    hide = models.BooleanField(default=False)


class Timetable(CMSPlugin):
    hide_past = models.BooleanField()
    show_vods = models.BooleanField()
