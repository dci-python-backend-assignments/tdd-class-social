from django.test import TestCase
from datetime import datetime
from social.models import BaseUser
from unittest import mock

class BaseUserModelTestCase(TestCase):

    def test_creating_a_new_user_200(self):
        user2 = BaseUser.objects.create(username="Kelly", password="12345", email="kelly@email.com", role="STD",
                                        address="Dresden", created_on="2022-08-19")
        user = BaseUser.objects.create(username="peter", password="12345", email="peter@email.com", role="STD",
                                       address="Dresden", created_on="2022-08-19", connections=user2)

        self.assertEqual(user.id, 2)
        self.assertEqual(user.username, "peter")
        self.assertEqual(user.password, "12345")
        self.assertEqual(user.email, "peter@email.com")
        self.assertEqual(user.created_on, "2022-08-19")
        self.assertEqual(user.is_active, False)
        self.assertEqual(user.address, "Dresden")
        self.assertEqual(user.website, None)
        self.assertEqual(user.about, None)
        self.assertEqual(user.connections, user2)
        self.assertEqual(user.role, "STD")

