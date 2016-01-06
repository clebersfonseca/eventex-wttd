from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class subscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Cleber Fonseca',
            cpf = '2345678901',
            email = 'cleber@3wsolution.com.br',
            phone = '53-99487480'
        )

        self.obj.save()
    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)