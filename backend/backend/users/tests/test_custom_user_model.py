from django.test import TestCase
from users.models import CustomUser


class CustomUserModelTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        CustomUser.objects.create(
            email='lola@tunesquad.com', name='Lola', last_name='Bunny',
            gov_id='10', company='Warner Bros',
            )
        CustomUser.objects.create(
            email='bugs@tunesquad.com', name='Bugs', last_name='Bunny',
            gov_id='1', company='Warner Bros',
            )

    def test_user_name(self):
        user_lola = CustomUser.objects.get(email='lola@tunesquad.com')
        user_bugs = CustomUser.objects.get(email='bugs@tunesquad.com')
        self.assertEqual(
            user_lola.get_name(),
            "User with email: lola@tunesquad.com has Lola as name.")
        self.assertEqual(
            user_bugs.get_name(),
            "User with email: bugs@tunesquad.com has Bugs as name.")
