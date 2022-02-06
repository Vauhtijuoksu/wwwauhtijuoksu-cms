from cms.models import CMSPlugin
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Player(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    nickname = models.CharField(max_length=30)
    discord = models.CharField(max_length=50)
    twitch = models.CharField(max_length=50, blank=True)

    allergies = models.TextField(blank=True)

    def __str__(self):
        return self.nickname


class Event(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    reg_open = models.DateTimeField(blank=True, null=True)
    reg_close = models.DateTimeField(blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True, null=True)

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
    game_title = models.CharField(max_length=100)
    publish_year = models.PositiveSmallIntegerField()
    console = models.CharField(max_length=29)
    console_display = models.CharField(max_length=29)

    # Run details
    category = models.CharField(max_length=100)
    estimate = models.CharField(max_length=20)
    description = models.TextField()
    video_link = models.URLField()
    scoreboard_link = models.URLField()

    # Extras
    time_constraints = models.TextField()
    for_children = models.BooleanField(default=False)
    flashing_lights = models.BooleanField(default=False)

    # Meta
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.game_title} {self.category} ({self.event})'


class MarathonPlugin(CMSPlugin):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
