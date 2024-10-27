from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from users.tests.factories import UserFactory
from ..models import Country
from .factories import CountryFactory
from posts.tests.factories import PostFactory


@mark.django_db
class CountryViewSetTest(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("country-list")
        self.detail_url: str = "country-detail"

    def test_countries_list(self):
        user = UserFactory()
        countries_without_posts = [CountryFactory() for _ in range(10)]
        countries = [CountryFactory() for _ in range(10)]
        posts = [PostFactory(country=country) for country in countries]

        self.client.force_login(user)
        with self.assertNumQueries(4):
            res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["count"], len(countries))

    def test_countries_list_as_non_authorized(self):
        countries = [CountryFactory() for _ in range(10)]
        with self.assertNumQueries(0):
            res = self.client.get(self.list_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_country_detail(self):
        user = UserFactory()
        country = CountryFactory()
        posts = [PostFactory(country=country) for _ in range(10)]

        self.client.force_login(user)
        with self.assertNumQueries(4):
            res = self.client.get(reverse(self.detail_url, kwargs={"slug": country.slug}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["name"], country.name)
        self.assertEqual(res_json["capital"], country.capital)
        self.assertEqual(len(res_json["posts"]), len(posts))

    def test_country_detail_as_non_authorized(self):
        country = CountryFactory()
        with self.assertNumQueries(0):
            res = self.client.get(reverse(self.detail_url, kwargs={"slug": country.slug}))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
