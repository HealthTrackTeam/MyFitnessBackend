from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
# from .models import Activity

class UserAuthTests(APITestCase):

    def test_register_user(self):
        url = reverse('auth_register')
        data = {"username": "john", "password": "12345"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="john").exists())

    #     ddd
def test_login_user(self):
    User.objects.create_user(username="john", password="12345")
    url = reverse('auth_login')
    data = {"username": "john", "password": "12345"}
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn("access", response.data)
    self.assertIn("refresh", response.data)