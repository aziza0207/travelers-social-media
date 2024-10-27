from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import CountryFactory, CountrySubscriptionFactory
from users.tests.factories import UserFactory
from countries.models import CountrySubscription


@mark.django_db
class CountrySubscriptionViewSetTest(APITestCase):
    def setUp(self):
        self.unsubscribe_url: str = "unsubscribe-country"
        self.subscribe_url: str = "subscribe-country"

    def test_subscribe_to_country(self):
        country = CountryFactory()
        user = UserFactory()
        self.client.force_login(user)
        self.assertEqual(CountrySubscription.objects.count(), 0)
        with self.assertNumQueries(11):
            res = self.client.post(
                reverse(self.subscribe_url, kwargs={"slug": country.slug})
            )
            res_json = res.json()
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertIn("Вы успешно подписались", res_json["detail"])
            self.assertEqual(CountrySubscription.objects.count(), 1)
            new_subscription = CountrySubscription.objects.first()
            self.assertEqual(new_subscription.user, user)
            self.assertEqual(new_subscription.country, country)

        with self.assertNumQueries(5):
            res = self.client.post(
                reverse(self.subscribe_url, kwargs={"slug": country.slug})
            )
            res_json = res.json()

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(CountrySubscription.objects.count(), 1)
            self.assertIn("Вы уже подписаны", res_json["detail"])

    def test_unsubscribe_to_country(self):
        country = CountryFactory()
        user = UserFactory()
        country_subscription = CountrySubscriptionFactory(country=country, user=user)
        self.client.force_login(user)
        self.assertEqual(CountrySubscription.objects.count(), 1)
        with self.assertNumQueries(6):
            res = self.client.delete(
                reverse(self.unsubscribe_url, kwargs={"slug": country.slug})
            )
            self.assertEqual(CountrySubscription.objects.count(), 0)
            self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertNumQueries(5):
            res = self.client.delete(
                reverse(self.unsubscribe_url, kwargs={"slug": country.slug})
            )
            self.assertEqual(CountrySubscription.objects.count(), 0)
            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
