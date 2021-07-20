from django.test import TestCase
from retail_company.models import User


class UserModelTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        User.objects.create(
            name='Maria', last_name='Lopez', government_issued_id='654321',
            email='maria@it.com', company='It'
            )
        User.objects.create(
            name='Pedro', last_name='Perez', government_issued_id='123654',
            email='peter@example.com', company='Big Co.'
            )

    def test_user_email(self):
        user_maria = User.objects.get(name='Maria')
        user_pedro = User.objects.get(name='Pedro')
        self.assertEqual(
            user_maria.get_email(), "Maria has maria@it.com as email.")
        self.assertEqual(
            user_pedro.get_email(), "Pedro has peter@example.com as email.")
