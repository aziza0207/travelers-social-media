from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User
from .factories import UserFactory
from posts.tests.factories import PostFactory
from posts.tests.factories import CountryFactory


@mark.django_db
class UserViewSetTest(APITestCase):
    def setUp(self):
        self.register_url: str = reverse("user-register")
        self.list_url: str = reverse("user-list")
        self.login_url: str = reverse("user-login")
        self.detail_url: str = "user-detail"

    def test_create_user(self):
        self.assertEqual(User.objects.count(), 0)
        payload = {
            "first_name": "TestUser",
            "last_name": "TestUserLastName",
            "email": "test-email@example.com",
            "password": "test-password",
        }
        with self.assertNumQueries(6):
            res = self.client.post(self.register_url, data=payload)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            res_json = res.json()
            self.assertEqual(User.objects.count(), 1)
            new_user = User.objects.first()
            self.assertEqual(new_user.first_name, payload["first_name"])
            self.assertEqual(new_user.last_name, payload["last_name"])
            self.assertEqual(new_user.email, payload["email"])
            self.assertNotIn("password", res_json)

    def test_user_login(self):
        payload = {
            "email": "test-user@example.com",
            "password": "test-password"
        }
        user = User.objects.create_user(**payload)
        with self.assertNumQueries(1):
            res = self.client.post(self.login_url, data=payload)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertIn("access_token", res.data)
            self.assertIn("refresh_token", res.data)

    def test_user_list(self):
        users = [UserFactory() for _ in range(10)]
        with self.assertNumQueries(2):
            res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["count"], len(users))

    def test_user_detail(self):
        user = UserFactory()
        country = CountryFactory()
        posts = [PostFactory(author=user, country=country) for _ in range(10)]

        with self.assertNumQueries(2):
            res = self.client.get(reverse(self.detail_url, kwargs={"pk": user.id}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["first_name"], user.first_name)
        self.assertEqual(res_json["last_name"], user.last_name)
        self.assertEqual(res_json["last_name"], user.last_name)
        self.assertEqual(len(res_json["posts"]), len(posts))
