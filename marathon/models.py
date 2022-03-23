from cms.models import CMSPlugin
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Player(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    nickname = models.CharField(_('nimimerkki'), max_length=30)
    discord = models.CharField(_('discord-tunnus'), max_length=50)
    twitch = models.CharField(_('twitch-tunnus'), max_length=50, blank=True)

    allergies = models.TextField(_('erityisruokavalio'), blank=True)

    def __str__(self):
        return self.nickname


class Event(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    reg_open = models.DateTimeField(blank=True, null=True)
    reg_close = models.DateTimeField(blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True, null=True)

    gdpr_notice = models.FileField(verbose_name=_("Tietosuojaseloste"), blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Submission(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name='submissions')

    # Game info
    game_title = models.CharField(_('peli'), max_length=100)
    publish_year = models.CharField(_('julkaisuvuosi'), max_length=10)
    console = models.CharField(_('laite/konsoli'), max_length=29)
    console_display = models.CharField(max_length=29, blank=True, null=True)

    # Run details
    category = models.CharField(_('kategoria'), max_length=100)
    estimate = models.CharField(_('aika-arvio'), max_length=20)
    description = models.TextField(_('perustelut'), blank=True)
    video_link = models.URLField(_('videolinkki'), blank=True)
    scoreboard_link = models.URLField(_('rankinglistalinkki'), blank=True)

    # Extras
    time_constraints = models.TextField(_('aikataulurajoitteet'), blank=True)
    for_children = models.BooleanField(_('sopiva lapsille'), default=False,
                                       help_text=_('Runin sisältö ja selostus ovat lapsiyleisölle sopivia'))
    flashing_lights = models.BooleanField(_('sisältää nopeasti vilkkuvia valoja'), default=False)

    # Mandatory
    gdpr = models.BooleanField(default=False)

    # Meta
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.game_title} {self.category} ({self.event})'


class MarathonPlugin(CMSPlugin):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
