from django.test import TestCase

from vj_cms.templatetags.vj_extras import render_duration


class TemplateTagCase(TestCase):
    def test_render_duration(self):
        test_cases = [
            [3600, '1h'],
            [0, ''],
            [3720, '1h 2min'],
            [37800, '10h 30min'],
            [3602, '1h 2sec']
        ]
        for case, output in test_cases:
            self.assertEqual(render_duration(case), output)