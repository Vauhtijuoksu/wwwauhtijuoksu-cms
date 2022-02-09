from django.contrib import admin

# Register your models here.
from marathon.models import Event, Player, Submission

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass