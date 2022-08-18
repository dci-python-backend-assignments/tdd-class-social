# from django.test import TestCase
# from datetime import datetime
# from social.models import BaseUser
# from unittest import mock
#
# class BaseUserModelTestCase(TestCase):
#
#     def test_creating_a_new_user_200(self):
#         # mock_date = datetime(2022, 8, 18, 12, 10, 10, 703055)
#         # with mock.patch('django.utils.timezone.now') as mock_now:
#         #     mock_now.return_value = mock_date
#         user = BaseUser.objects.create(username="peter", password="12345", email="peter@email.com", role="STD",
#                                        address="Dresden", )
#
#         self.assertEqual(user.id, 1)
#         self.assertEqual(user.username, "peter")
#         self.assertEqual(user.password, "12345")
#         self.assertEqual(user.email, "peter@email.com")
#         # self.assertEqual(user.created_on, mock_date) # ask how to test this
#         self.assertEqual(user.is_active, False)
#         self.assertEqual(user.address, None)
#         self.assertEqual(user.website, None)
#         self.assertEqual(user.about, None)
#         # self.assertEqual(user.connections, None) # ask how to test this
#
#     def test_new_user_has_duplicate_email_fail(self):
#         # mock_date = datetime(2022, 8, 18, 12, 10, 10, 703055)
#         # with mock.patch('django.utils.timezone.now') as mock_now:
#         #     mock_now.return_value = mock_date
#         user1 = BaseUser.objects.create(username="peter", password="12345", email="peter@email.com", role="STD")
#         user2 = BaseUser.objects.create(username="kelly", password="54321", email="peter@email.com", role="STD")
#
#         self.assertEqual(user2.id, 2)
#         self.assertEqual(user2.username, "kelly")
#         self.assertEqual(user2.password, "54321")
#         self.assertEqual(user2.email, "peter@email.com")
#         # self.assertEqual(user.created_on, mock_date) # ask how to test this
#         self.assertEqual(user2.is_active, False)
#         self.assertEqual(user2.address, None)
#         self.assertEqual(user2.website, None)
#         self.assertEqual(user2.about, None)
#         # self.assertEqual(user.connections, None) # ask how to test this
