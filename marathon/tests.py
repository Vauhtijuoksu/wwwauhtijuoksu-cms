import datetime

from django.test import TestCase
from marathon.models import *


# Create your tests here.

class EventTestCase(TestCase):
    def setUp(self):
        pass

    def test_slug_autogeneration(self):
        event = Event.objects.create(name='Vauhtijuoksu 2022', start=datetime.date.today())
        self.assertEqual(event.slug, 'vauhtijuoksu-2022')

    def test_manual_slug(self):
        event = Event.objects.create(name='Manual', slug='test-slug')
        self.assertEqual(event.slug, 'test-slug')
