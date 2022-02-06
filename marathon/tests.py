import datetime

from django.test import Client, TestCase, override_settings
from . import urls
from .models import *

# Create your tests here.

@override_settings(ROOT_URLCONF=urls)
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name='Vauhtijuoksu 2022', start=datetime.date.today())

    def test_slug_autogeneration(self):
        event = Event.objects.get(name='Vauhtijuoksu 2022')
        self.assertEqual(event.slug, 'vauhtijuoksu-2022')

    def test_manual_slug(self):
        event = Event.objects.create(name='Manual', slug='test-slug')
        self.assertEqual(event.slug, 'test-slug')

    def test_event_details(self):
        response = self.client.get('/vauhtijuoksu-2022/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['event'].name, 'Vauhtijuoksu 2022')

    def test_new_submission_view_render(self):
        response = self.client.get('/vauhtijuoksu-2022/submission/')
        self.assertEqual(response.status_code, 200)