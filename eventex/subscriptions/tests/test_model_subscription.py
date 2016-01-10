from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class subscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Cleber Fonseca',
            cpf = '12345678901',
            email = 'cleber@3wsolution.com.br',
            phone = '53-99487480'
        )

        self.obj.save()


    def test_create(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)


    def test_str(self):
        self.assertEqual('Cleber Fonseca', str(self.obj))


    def test_paid_default_to_false(self):
        """By default paid must False"""
        self.assertEqual(False, self.obj.paid)