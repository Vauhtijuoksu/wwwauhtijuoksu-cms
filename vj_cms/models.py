from collections import defaultdict

from cms.models import CMSPlugin
from django.db import models

class GameInfo(models.Model):
    # From API
    api_id = models.UUIDField(primary_key=True)
    game = models.CharField('name', max_length=255)
    category = models.CharField('category', null=True, blank=True, max_length=255)
    device = models.CharField('device', null=True, blank=True, max_length=255)
    players = models.ManyToManyField('PlayerInfo', related_name='games')
    player = models.CharField('player nick', null=True, blank=True, max_length=255)
    player_twitch = models.CharField('twitch', null=True, blank=True, max_length=255)
    published = models.CharField('publishing year', null=True, blank=True, max_length=255)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True, blank=True)
    vod_link = models.URLField(null=True, blank=True)
    img_filename = models.CharField(null=True, blank=True, max_length=127)
    meta = models.CharField(null=True, default="", max_length=255)

    # Custom added fields
    icon = models.ImageField(null=True, blank=True)
    estimate = models.PositiveIntegerField('estimate in seconds', default=0, null=True, blank=True)
    hide = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.estimate = (self.end_time - self.start_time).total_seconds()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.game

    def _meta_field(self, field):
        return self.meta and field in self.meta.split(',')

    @property
    def childsafe(self):
        return self._meta_field('childsafe')

    @property
    def flashing(self):
        return self._meta_field('flashing')

class PlayerInfo(models.Model):
    api_id = models.UUIDField(primary_key=True)
    discord_nick = models.CharField(null=True, default="", max_length=255)
    display_name = models.CharField(null=True, default="", max_length=255)
    twitch_channel = models.CharField(null=True, default="", max_length=255)


class Timetable(CMSPlugin):
    hide_past = models.BooleanField()
    show_vods = models.BooleanField()


class Donatebar(CMSPlugin):
    goal = models.PositiveIntegerField('Goal', default=1000)


class AnchorLink(CMSPlugin):
    anchor_tag = models.CharField("Anchor tag", null=True, default="", max_length=255)
    title = models.CharField("Title in menu (Empty = hidden)", null=True, default="", max_length=255)

class TweakSettings(CMSPlugin):
    message_duration = models.PositiveIntegerField('Carousel message duration (seconds)', default=8)
    show_scrolldown_menu = models.BooleanField('Show scrolldown menu', default=False)
    show_login = models.BooleanField('Show login', default=True)

class SponsorLogoHolder(CMSPlugin):
    size = models.CharField("Logo size (L/M/S)", default="M", max_length=1)