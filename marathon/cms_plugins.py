from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import SubmissionForm, PlayerForm
from .models import Event, Submission, MarathonPlugin

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

        form = SubmissionForm()
        player_form = PlayerForm(prefix='player')

        context['form'] = form
        context['player_form'] = player_form
        context['event'] = instance.event
        return context