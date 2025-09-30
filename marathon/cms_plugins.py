import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import SubmissionForm, PlayerForm
from .models import Event, Submission, MarathonPlugin, Player
from .utils import get_player_info_for_user

class SubmissionListSubmission:
    def __init__(self, submission):
        self.game_title = submission.game_title
        self.category = submission.category
        self.players = []
        self.estimate = submission.estimate
        self.ptest = ""
        self.ntest = ""
        for player in submission.players.all():
            self.ptest += str(player.user_id) + " "
            self.ntest += player.nickname + " "
            self.atest = player
            p = Player.objects.filter(user_id=player.user_id).first()
            self.players.append(SubmissionListPlayer(p))

    def update(self, submission):
        for player in submission.players.all():
            found = False
            for p in self.players:
                if p.user_id == player.user_id:
                    found = True
                    break
            if not found:
                self.players.append(SubmissionListPlayer(player))
        ctime = self.estimate.split(":")
        stime = submission.estimate.split(":")
        if len(ctime) == 2 and len(stime) == 2:
            crun_time = int(ctime[0]) * 60 + int(ctime[1])
            srun_time = int(stime[0]) * 60 + int(stime[1])
            if crun_time < srun_time:
                self.estimate = submission.estimate
                return srun_time - crun_time
        return 0


class SubmissionListPlayer:
    def __init__(self, player):
        self.nickname = player.nickname
        self.twitch = player.twitch
        self.user_id = player.user_id


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
        total_time = 0
        unique_submissions = {}
        for s in submissions:
            for p in s.players.all():
                if p.user_id not in unique_players:
                    unique_players.append(p.user_id)
            run_id = s.game_title.lower() + s.category.lower()
            if run_id not in unique_submissions:
                unique_submissions[run_id] = SubmissionListSubmission(s)
                time = s.estimate.split(":")
                if len(time) == 2:
                    total_time += int(time[0]) * 60 + int(time[1])
            else:
                total_time += unique_submissions[run_id].update(s)

        total_days = int(total_time / 60 / 24)
        total_hours = int(total_time / 60) % 24
        total_minutes = total_time % 60
        time_string = str(total_hours) + " t " + str(total_minutes) + " m"
        if total_days > 0:
            time_string = str(total_days) + " p " + str(total_hours) + "." + str(int(total_minutes/6)) + " t"

        u_subs = unique_submissions.values()
        context['submissions'] = u_subs
        context['game_count'] = str(len(u_subs))
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