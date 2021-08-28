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


class CreateNewUserTest(TestCase):
    """ Test module for inserting a new user """
    def setUp(self):
        self.valid_payload = {
            "name": "Willie E.",
            "last_name": "Coyote",
            "gov_id": "13",
            "email": "coyote@tunesquad.com",
            "company": "Warner Bros"
            }
        self.invalid_payload = {
            "name": "Taz",
            "last_name": "",
            "gov_id": "!",
            "email": "taz@tunesquad.com",
            "company": "Warner Bros"
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

    def test_get_valid_single_user(self):
        # get API response
        response = client.get(
            reverse('get_user', kwargs={'pk': self.willie.pk}))
        # get data from db
        user = CustomUser.objects.get(pk=self.willie.pk)
        serializer = CustomUserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_user(self):
        response = client.get(
            reverse('get_user', kwargs={'pk': 666}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


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
