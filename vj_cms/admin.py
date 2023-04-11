from django.contrib import admin

from vj_cms.models import GameInfo, PlayerInfo


@admin.register(GameInfo)
class GameInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(PlayerInfo)
class PlayerInfoAdmin(admin.ModelAdmin):
    pass
