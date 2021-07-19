import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from retail_company.models import User
from retail_company.serializers import UserSerializer


# initialize the APIClient app
client = Client()


class CreateNewUserTest(TestCase):
    """ Test module for inserting a new user """
    def setUp(self):
        self.valid_payload = {
            'name': 'Mary',
            'last_name': 'Mena',
            'government_issued_id': "654321",
            "email": "mary@dea.com",
            "company": "DEA"
        }
        self.invalid_payload = {
            'name': '',
            'last_name': 'Lopez',
            'government_issued_id': "123456",
            "email": "peter@it.com",
            "company": "It company"
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('post_user'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('post_user'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
