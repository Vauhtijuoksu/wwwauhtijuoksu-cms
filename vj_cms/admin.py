from django.contrib import admin

from vj_cms.models import GameInfo


@admin.register(GameInfo)
class GameInfoAdmin(admin.ModelAdmin):
    pass
