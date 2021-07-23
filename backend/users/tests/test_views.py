import json
from django.http import response
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from users.views import get_users


# initialize the APIClient app
client = Client()

'''
class CreateNewUserTest(TestCase):
    """ Test module for inserting a new user """
    def setUp(self):
        self.valid_payload = {
            "name": "Mary",
            "last_name": "Mena",
            "government_issued_id": "654321",
            "email": "mary@example.com",
            "company": ""
        }
        self.invalid_payload = {
            "name": "",
            "last_name": "Lopez",
            "government_issued_id": "123456",
            "email": "peter@it.com",
            "company": "It company"
        }

    def test_create_valid_user(self):
        # get API response
        response = client.post(
            reverse("post_user"),
            data=json.dumps(self.valid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse("post_user"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleUserTest(TestCase):
    """ Test module for GET single user API """
    def setUp(self):
        self.maria = User.objects.create(
            name='Maria', last_name='Lopez', government_issued_id='654321',
            email='maria@it.com', company='It'
            )
        self.pedro = User.objects.create(
            name='Pedro', last_name='Perez', government_issued_id='123654',
            email='peter@example.com', company='Big Co.'
            )
        self.lola = User.objects.create(
            name='Lola', last_name='Bunny', government_issued_id='458645',
            email='lola@wb.com', company='Warner Bros.'
            )
        self.pedro = User.objects.create(
            name='John', last_name='Doe', government_issued_id='666666',
            email='jd@unknown.com', company=''
            )

    def test_get_valid_single_user(self):
        # get API response
        response = client.get(
            reverse('get_update_delete_user', kwargs={'pk': self.lola.pk}))
        # get data from db
        user = User.objects.get(pk=self.lola.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        response = client.get(
            reverse('get_update_delete_user', kwargs={'pk': 666}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

'''


class GetAllUsersTest(TestCase):
    """ Test module for GET all users API """
    def setUp(self):
        self.lola = CustomUser.objects.create(
            email='lola@tunesquad.com',
            name='Lola', last_name='Bunny',
            gov_id='10', company='Warner Bros'
            )
        self.bugs = CustomUser.objects.create(
            email='bugs@tunesquad.com',
            name='Bugs', last_name='Bunny',
            gov_id='1', company='Warner Bros'
            )
        self.willie = CustomUser.objects.create(
            email='coyote@tunesquad.com',
            name='Willi E.', last_name='Coyote',
            gov_id='13', company='Warner Bros'
            )
        self.taz = CustomUser.objects.create(
            email='taz@tunesquad.com',
            name='Taz', last_name='',
            gov_id='', company='Warner Bros'
            )

    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('get_users'))
        # get data from db
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
