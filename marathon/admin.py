from django.contrib import admin

# Register your models here.
from marathon.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
