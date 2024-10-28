from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import TagFactory, TagSubscriptionFactory
from users.tests.factories import UserFactory
from tags.models import TagSubscription


@mark.django_db
class TagSubscriptionViewSetTest(APITestCase):
    def setUp(self):
        self.unsubscribe_url: str = "unsubscribe-tag"
        self.subscribe_url: str = "subscribe-tag"

    def test_subscribe_to_tag(self):
        tag = TagFactory()
        user = UserFactory()
        self.client.force_login(user)
        self.assertEqual(TagSubscription.objects.count(), 0)
        with self.assertNumQueries(11):
            res = self.client.post(
                reverse(self.subscribe_url, kwargs={"slug": tag.slug})
            )
            res_json = res.json()
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            self.assertIn("Вы успешно подписались", res_json["detail"])
            self.assertEqual(TagSubscription.objects.count(), 1)
            new_subscription = TagSubscription.objects.first()
            self.assertEqual(new_subscription.user, user)
            self.assertEqual(new_subscription.tag, tag)

        with self.assertNumQueries(5):
            res = self.client.post(
                reverse(self.subscribe_url, kwargs={"slug": tag.slug})
            )
            res_json = res.json()

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(TagSubscription.objects.count(), 1)
            self.assertIn("Вы уже подписаны", res_json["detail"])

    def test_unsubscribe_to_tag(self):
        tag = TagFactory()
        user = UserFactory()
        tag_subscription = TagSubscriptionFactory(tag=tag, user=user)
        self.client.force_login(user)
        self.assertEqual(TagSubscription.objects.count(), 1)
        with self.assertNumQueries(6):
            res = self.client.delete(
                reverse(self.unsubscribe_url, kwargs={"slug": tag.slug})
            )
            self.assertEqual(TagSubscription.objects.count(), 0)
            self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertNumQueries(5):
            res = self.client.delete(
                reverse(self.unsubscribe_url, kwargs={"slug": tag.slug})
            )
            self.assertEqual(TagSubscription.objects.count(), 0)
            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)