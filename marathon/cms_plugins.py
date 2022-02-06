from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import SubmissionForm, PlayerFormSet
from .models import Event, Submission, MarathonPlugin

@plugin_pool.register_plugin
class SubmissionListPlugin(CMSPluginBase):
    name = 'Submission List'
    model = MarathonPlugin
    render_template = 'marathon/plugins/submission_list.html'

    def render(self, context, instance, placeholder):
        context = super().render(self, context, instance, placeholder)

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

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        players_formset = PlayerFormSet()
        form = SubmissionForm()
        context['form'] = form
        context['players_formset'] = players_formset
        return context