from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)

    nickname = models.CharField(max_length=30)
    discord = models.CharField(max_length=50)
    twitch = models.CharField(max_length=50)

    allergies = models.TextField()


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
    players = models.ManyToManyField(Player)

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
    age_restrictions = models.CharField(max_length=250)
    warnings = models.CharField(max_length=250)

    # Meta
    hidden = models.BooleanField(default=False)

