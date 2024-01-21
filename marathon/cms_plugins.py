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

        form = SubmissionForm(previous_data)
        if previous_data:
            player_form = PlayerForm(previous_data, prefix='player')
        elif context['request'].user.is_authenticated:
            print('got user')
            player_info = get_player_info_for_user(context['request'].user)
            player_form = PlayerForm(initial=player_info, prefix='player')
        else:
            player_form = PlayerForm(prefix='player')
        context['require_authentication'] = True
        context['form'] = form
        context['player_form'] = player_form
        context['event'] = instance.event
        return context