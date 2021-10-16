from random import randint, shuffle, random
import math
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from vj_cms.models import GameInfo, Timetable
from datetime import datetime

@plugin_pool.register_plugin
class DividerPlugin(CMSPluginBase):
    name = 'Divider'
    model = CMSPlugin
    render_template = "vauhtijuoksu/plugins/divider.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['number'] = randint(0, 3)
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
            if day_was != game.start_time.strftime("%m.%d.%Y"):
                day_was = game.start_time.strftime("%m.%d.%Y")
                if day:
                    days.append(day[:])
                day = []
            day.append(game)
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