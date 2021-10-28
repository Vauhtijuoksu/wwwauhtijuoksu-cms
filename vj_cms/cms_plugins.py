from random import randint, shuffle, random
import math
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from vj_cms.client import LegacyClient
from vj_cms.models import GameInfo, Timetable
from datetime import datetime
import requests

legacy_client = LegacyClient(settings.VJ_LEGACY_API_URL)

@plugin_pool.register_plugin
class DividerPlugin(CMSPluginBase):
    name = 'Divider'
    model = CMSPlugin
    render_template = "vauhtijuoksu/plugins/divider.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['divider_name'] = f'divider_{randint(0, 3)}.png'
        return context

@plugin_pool.register_plugin
class TimetablePlugin(CMSPluginBase):
    name = 'Timetable'
    model = Timetable
    render_template = "vauhtijuoksu/plugins/timetable.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        games = GameInfo.objects.all().order_by('start_time')
        days = []
        day_was = ""
        day = []
        for game in games:
            if day_was != game.start_time.astimezone().strftime("%m.%d.%Y"):
                day_was = game.start_time.astimezone().strftime("%m.%d.%Y")
                if day:
                    days.append(day[:])
                day = []
            day.append(game)
        if day:
            days.append(day[:])
        context['games'] = days[:]
        return context


@plugin_pool.register_plugin
class TabletimetablePlugin(CMSPluginBase):
    name = 'Tabletimetable'
    model = CMSPlugin
    render_template = "vauhtijuoksu/plugins/tabletimetable.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        games = GameInfo.objects.all().order_by('start_time')
        days = []
        day_was = ""
        day = []
        for game in games:
            data = {
                "game": game.game,
                "img_filename": game.img_filename,
                "player": game.player,
                "player_twitch": game.player_twitch,
                "category": game.category,
                "start_time":  game.start_time,
                "end_time":  game.end_time,
                "estimate":  game.estimate
            }
            if day_was != game.start_time.astimezone().strftime("%m.%d.%Y"):
                day_was = game.start_time.astimezone().strftime("%m.%d.%Y")
                if day:
                    days.append(day[:])
                day = []
            # cut night games
            if day_was != game.end_time.astimezone().strftime("%m.%d.%Y"):
                day_was = game.end_time.astimezone().strftime("%m.%d.%Y")
                start_percent = (game.start_time.astimezone().hour * 60 + game.start_time.astimezone().minute) / (24 * 60) * 100
                end_percent = 0
                start = {
                    "start_percent": start_percent,
                    "end_percent": end_percent,
                    "cut_style": "end-cut"
                }
                start.update(data)
                day.append(start)
                days.append(day[:])
                day = []
                start_percent = 0
                end_percent = 100-(game.end_time.astimezone().hour * 60 + game.end_time.astimezone().minute)/(24*60) * 100
                end = {
                    "start_percent": start_percent,
                    "end_percent": end_percent,
                    "cut_style": "start-cut"
                }
                end.update(data)
                day.append(end)
            else:
                start_percent = (game.start_time.astimezone().hour * 60 + game.start_time.astimezone().minute)/(24*60) * 100
                end_percent = 100-(game.end_time.astimezone().hour * 60 + game.end_time.astimezone().minute)/(24*60) * 100
                data.update({
                    "start_percent": start_percent,
                    "end_percent": end_percent,
                    "cut_style": ""
                })
                day.append(data)
        if day:
            days.append(day[:])
        context['games'] = days[:]
        return context

@plugin_pool.register_plugin
class FloatycharsPlugin(CMSPluginBase):
    name = 'Floatychars'
    model = CMSPlugin
    render_template = "vauhtijuoksu/plugins/floatychars.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        games = list(GameInfo.objects.all())
        chars = []
        i = 0
        shuffle(games)
        for game in games:
            if game.img_filename and game.img_filename != "placeholder.png":
                offset = 0.4* math.atan(6*random()-3)+0.5
                opacity = 0.1 + 0.6*2*abs(offset - 0.5)
                xscale = (randint(0,1)-0.5)*4
                top = 2+ (96/len(games))*i + (50/len(games))*random()
                chars.append({
                    "file": game.img_filename,
                    "left":str(offset*90+5) + "%",
                    "top": str(top) + "%",
                    "xscale": xscale,
                    "opacity": opacity,
                    "delay": str(random()*-6)+"s",
                })
            i+=1
        context['chars'] = chars
        return context
    

@plugin_pool.register_plugin
class IncentivesPlugin(CMSPluginBase):
    #Whole incentive system is still using the legacy api so it will change later
    name = 'Incentives'
    model = CMSPlugin
    render_template = "vauhtijuoksu/plugins/incentives.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        incentives = legacy_client.incentives()

        context['incentives'] = incentives[:]
        return context