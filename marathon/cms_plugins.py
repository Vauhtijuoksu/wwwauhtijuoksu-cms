import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import SubmissionForm, PlayerForm
from .models import Event, Submission, MarathonPlugin
from .utils import get_player_info_for_user

@plugin_pool.register_plugin
class SubmissionListPlugin(CMSPluginBase):
    name = 'Submission List'
    model = MarathonPlugin
    render_template = 'marathon/plugins/submission_list.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        if instance.event:
            submissions = Submission.objects.filter(event=instance.event, hidden=False)
        else:
            submissions = Submission.objects.filter(hidden=False)

        unique_players = []
        run_times = {}
        total_time = 0
        for s in submissions:
            for p in s.players.all():
                if p not in unique_players:
                    unique_players.append(p)
            time = s.estimate.split(":")
            if len(time) == 2:
                run_id = s.game_title.lower() + s.category.lower()
                run_time = int(time[0]) * 60 + int(time[1])
                if run_id in run_times:
                    if run_times[run_id] < run_time:
                        total_time -= run_times[run_id]
                        run_times[run_id] = run_time
                        total_time += run_time
                else:
                    run_times[run_id] = run_time
                    total_time += run_time
        total_days = int(total_time / 60 / 24)
        total_hours = int(total_time / 60) % 24
        total_minutes = total_time % 60
        time_string = str(total_hours) + " t " + str(total_minutes) + " m"
        if total_days > 0:
            time_string = str(total_days) + " p " + str(total_hours) + "." + str(int(total_minutes/6)) + " t"

        context['submissions'] = submissions
        context['game_count'] = str(len(run_times))
        context['unique_players'] = str(len(unique_players))
        context['total_run_time'] = time_string
        return context


@plugin_pool.register_plugin
class MySubmissionsPlugin(CMSPluginBase):
    name = 'My Submissions'
    model = MarathonPlugin
    render_template = 'marathon/plugins/my_submissions.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        if context['request'].user.is_authenticated:
            player_id = get_player_info_for_user(context['request'].user).get('id')
        else:
            player_id = None

        if instance.event and player_id:
            submissions = Submission.objects.filter(event=instance.event, hidden=False, players__in=[player_id])
        else:
            submissions = {}

        context['require_authentication'] = True
        context['event'] = instance.event
        context['submissions'] = submissions
        return context


@plugin_pool.register_plugin
class SubmissionFormPlugin(CMSPluginBase):
    name = 'Submission Form'
    model = MarathonPlugin
    render_template = 'marathon/plugins/submission_form.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        previous_data = context['request'].session.get('previous_form')
        if context['request'].user.is_authenticated and not previous_data:
            player_id = get_player_info_for_user(context['request'].user).get('id')
            if player_id:
                last_submit = Submission.objects.filter(event=instance.event, hidden=False, players__in=[player_id]).last()
                if last_submit:
                    form = SubmissionForm(initial={'time_constraints': last_submit.time_constraints})
                else:
                    form = SubmissionForm()
            else:
                form = SubmissionForm()
        else:
            form = SubmissionForm(previous_data)

        if previous_data:
            player_form = PlayerForm(previous_data, prefix='player')
        elif context['request'].user.is_authenticated:
            player_info = get_player_info_for_user(context['request'].user)
            player_form = PlayerForm(initial=player_info, prefix='player')
            if player_info.get('discord'):
                player_form.fields['discord'].widget.attrs['readonly'] = True
        else:
            player_form = PlayerForm(prefix='player')


        event_duration = (instance.event.end - instance.event.start).days
        event_days = []
        for d in range(event_duration + 1):
            event_days.append(instance.event.start + datetime.timedelta(days=d))
        context['require_authentication'] = True
        context['form'] = form
        context['player_form'] = player_form
        context['event'] = instance.event
        context['event_days'] = event_days
        return context