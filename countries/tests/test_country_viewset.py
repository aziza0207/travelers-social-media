from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Country
from .factories import CountryFactory
from posts.tests.factories import PostFactory


@mark.django_db
class CountryViewSetTest(APITestCase):
    def setUp(self):
        self.list_url: str = reverse("country-list")
        self.detail_url: str = "country-detail"

    def test_user_list(self):
        countries_without_posts = [CountryFactory() for _ in range(10)]
        countries = [CountryFactory() for _ in range(10)]
        posts = [PostFactory(country=country) for country in countries]
        with self.assertNumQueries(2):
            res = self.client.get(self.list_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["count"], len(countries))

    def test_user_detail(self):
        country = CountryFactory()
        posts = [PostFactory(country=country) for _ in range(10)]

        with self.assertNumQueries(2):
            res = self.client.get(reverse(self.detail_url, kwargs={"pk": country.id}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["name"], country.name)
        self.assertEqual(res_json["capital"], country.capital)
        self.assertEqual(len(res_json["posts"]), len(posts))
